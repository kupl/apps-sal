import sys

for _ in range(int(input())):
    k = int(input())
    a = input()
    res = 0
    cur = k - 1
    for i in range(k - 1, -1, -1):
        if a[i] == 'A':
            res = max(res, cur - i)
            cur = -1
        else:
            cur = max(cur, i)
    print(res)
