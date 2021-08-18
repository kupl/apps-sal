N = int(input())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

total_table = {}


def make_table(l):
    table = {}
    for v in l:
        if v in table:
            table[v] += 1
        else:
            table[v] = 1
        if v in total_table:
            total_table[v] += 1
        else:
            total_table[v] = 1
    return table


A_table = make_table(A_list)
B_table = make_table(B_list)

total_list = []
for v, c in list(total_table.items()):
    total_list.append((c, v))

total_list.sort()
total_list.reverse()

A_head = []
A_tail = []
B_head = []
B_tail = []
for c, v in total_list:
    a = A_table[v] if v in A_table else 0
    b = B_table[v] if v in B_table else 0
    while a > 0 and len(A_head) + len(B_head) < N:
        A_head.append(v)
        a -= 1

    while b > 0 and len(A_head) + len(B_head) < N:
        B_head.append(v)
        b -= 1

    while a > 0:
        A_tail.append(v)
        a -= 1

    while b > 0:
        B_tail.append(v)
        b -= 1


A_tail.reverse()
B_head.reverse()

A_list = A_head + A_tail
B_list = B_tail + B_head


def check():
    for a, b in zip(A_list, B_list):
        if a == b:
            return False
    else:
        return True


if check():
    AB_list = list(zip(A_list, B_list))
    AB_list.sort()
    print("Yes")
    print((*(b for a, b in AB_list)))
else:
    print("No")
