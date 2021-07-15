import sys

input = sys.stdin.readline

n = int(input())

s_list = []
not_10_s_list = []

for _ in range(n):
    s = int(input())
    if not s % 10 == 0:
        not_10_s_list.append(s)
    s_list.append(s)

if len(not_10_s_list) == 0:
    print(0)
    return

else:
    sum_s = sum(s_list)
    if not sum_s % 10 == 0:
        max_s = sum_s
        print(max_s)
        return

    max_s = -1
    for not_10_s in not_10_s_list:
        if not sum_s - not_10_s % 10 == 0:
            max_s = max(max_s,sum_s - not_10_s)
    print(max_s)
    return
