from math import gcd as bltin_gcd


def cp(a, b):
    return bltin_gcd(a, b) == 1


(n, m) = [int(x) for x in input().split()]
ans = []
yes = 'Possible'
no = 'Impossible'


def pri():
    print(yes)
    for x in ans:
        print(x[0], ' ', x[1])


if m < n - 1:
    print(no)
    quit()
if m == n - 1:
    print(yes)
    for i in range(1, m + 1):
        print(i, ' ', i + 1)
    quit()
for i in range(1, n):
    ans.append((i, i % n + 1))
for i in range(1, n + 1):
    for j in range(i + 2, n + 1):
        if i % 2 == 0 and j % 2 == 0:
            continue
        if cp(i, j):
            ans.append((i, j))
            if len(ans) == m:
                pri()
                quit()
print(no)
