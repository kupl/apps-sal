def solve1(s):
    evens = [u for u in s if u % 2 == 0]
    odds = [u for u in s if u % 2 == 1]
    if len(odds) == 0:
        return evens
    ans = []
    inserted_odd = 0
    current_odd = odds[inserted_odd]
    for i in range(len(evens)):
        while current_odd < evens[i] and inserted_odd < len(odds):
            ans.append(current_odd)
            inserted_odd += 1
            if inserted_odd < len(odds):
                current_odd = odds[inserted_odd]
        ans.append(evens[i])
    while inserted_odd < len(odds):
        ans.append(current_odd)
        inserted_odd += 1
        if inserted_odd < len(odds):
            current_odd = odds[inserted_odd]
    return ans


def solve2(s):
    odds = [u for u in s if u % 2 == 0]
    evens = [u for u in s if u % 2 == 1]
    if len(odds) == 0:
        return evens
    ans = []
    inserted_odd = 0
    current_odd = odds[inserted_odd]
    for i in range(len(evens)):
        while current_odd < evens[i] and inserted_odd < len(odds):
            ans.append(current_odd)
            inserted_odd += 1
            if inserted_odd < len(odds):
                current_odd = odds[inserted_odd]
        ans.append(evens[i])
    while inserted_odd < len(odds):
        ans.append(current_odd)
        inserted_odd += 1
        if inserted_odd < len(odds):
            current_odd = odds[inserted_odd]
    return ans


for _ in range(int(input())):
    s = list(map(int, list(input())))
    ans = min(solve1(s), solve2(s))
    print(''.join(map(str, ans)))
