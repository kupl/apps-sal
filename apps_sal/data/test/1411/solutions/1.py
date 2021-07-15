from collections import namedtuple


Member = namedtuple('Member', ['parts', 'a_happy', 'b_happy'])


def happy_diff(m):
    return m.a_happy - m.b_happy


def main():
    input_strings_members, parts = read_input()
    a_members, b_members, other_members = prepare_members(input_strings_members)
    print(count_parts(a_members, b_members, other_members, parts))


def read_input():
    counts_str = input().split()
    members_count, parts = list(map(int, counts_str))
    return [input() for _ in range(members_count)], parts


def prepare_members(input_strings_members):
    a_members = []
    b_members = []
    other_members = []
    for line in input_strings_members:
        m = Member(*list(map(int, line.split())))
        if happy_diff(m) > 0:
            a_members.append(m)
        elif happy_diff(m) < 0:
            b_members.append(m)
        else:
            other_members.append(m)
    return a_members, b_members, other_members


def count_parts(a_members, b_members, other_members, parts_in_one):
    a_members.sort(key=lambda m: happy_diff(m), reverse=False)
    a_modulo = sum(m.parts for m in a_members) % parts_in_one

    a_modulo_members, a_happy_members = split_members_into_happy_groups(a_members, a_modulo)
    a_happy = sum(m.a_happy * m.parts for m in a_happy_members)

    b_members.sort(key=lambda m: happy_diff(m), reverse=True)
    b_modulo = sum(m.parts for m in b_members) % parts_in_one

    b_modulo_members, b_happy_members = split_members_into_happy_groups(b_members, b_modulo)
    b_happy = sum(m.b_happy * m.parts for m in b_happy_members)

    last_happy = count_last_pizzas_happy(a_modulo_members, b_modulo_members, other_members, parts_in_one)

    return a_happy + b_happy + last_happy


def split_members_into_happy_groups(members, modulo):
    modulo_members = []
    happy_members = []
    current_modulo = 0

    for i in range(len(members)):
        m = members[i]
        new_current_modulo = current_modulo + m.parts
        if new_current_modulo < modulo:
            modulo_members.append(m)
            current_modulo = new_current_modulo
            continue

        modulo_members.append(Member(modulo - current_modulo, m.a_happy, m.b_happy))
        if new_current_modulo > modulo:
            happy_members.append(Member(new_current_modulo - modulo, m.a_happy, m.b_happy))
        if (i + 1) < len(members):
            happy_members.extend(members[(i + 1):])
        break

    return modulo_members, happy_members


def count_last_pizzas_happy(a, b, other, parts_in_one):
    last_sorted_members = a + other + b

    if sum(m.parts for m in last_sorted_members) <= parts_in_one:
        return max(
            sum(m.a_happy * m.parts for m in last_sorted_members),
            sum(m.b_happy * m.parts for m in last_sorted_members)
        )

    return sum(m.a_happy * m.parts for m in a + other) + sum(m.b_happy * m.parts for m in b)


def test1():
    a, b, c = prepare_members(['7 4 7', '5 8 8', '12 5 8', '6 11 6', '3 3 7', '5 9 6'])
    assert count_parts(a, b, c, 10) == 314


def test2():
    a, b, c = prepare_members(['3 5 7', '4 6 7', '5 9 5'])
    assert count_parts(a, b, c, 12) == 84


def test3():
    a, b, c = prepare_members(['2 3 1', '2 2 2', '2 1 3'])
    assert count_parts(a, b, c, 3) == 16


def test4():
    a, b, c = prepare_members(
        [
            '2 1 4',
            '2 3 1',
        ]
    )
    assert count_parts(a, b, c, 3) == 14


def test5():
    a, b, c = prepare_members(
        [
            '2 1 2',
            '2 2 1',
            '2 1 3',
            '2 3 1',
            '2 1 4',
            '2 4 1',
        ]
    )
    assert count_parts(a, b, c, 3) == (8 + 6 + 4) * 2


def test6():
    a, b, c = prepare_members(
        [
            '2 1 2',
            '2 2 1',
            '2 1 3',
            '2 3 1',
            '2 1 4',
            '2 4 1',
        ]
    )
    assert count_parts(a, b, c, 5) == 16 + 16 + 3


def test_without_last_pizzas():
    a, b, c = prepare_members(
        [
            '3 3 1',
            '3 5 6'
        ]
    )
    assert count_parts(a, b, c, 3) == 27


def test_with_one_last_pizza():
    a, b, c = prepare_members(
        [
            '2 3 1',
            '1 5 6'
        ]
    )
    assert count_parts(a, b, c, 3) == 11


def test_with_two_last_pizzas():
    a, b, c = prepare_members(
        [
            '2 3 4',
            '2 3 1',
            '1 1 1'
        ]
    )
    assert count_parts(a, b, c, 3) == 15


def test_without_different_happies():
    a, b, c = prepare_members(
        [
            '2 2 2',
            '4 1 1',
            '5 6 6'
        ]
    )
    assert count_parts(a, b, c, 3) == 38


def __starting_point():
    main()

__starting_point()
