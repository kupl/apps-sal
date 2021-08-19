# https://codeforces.com/contest/1183/problem/F


def solve(a_s):
    a_s = set(a_s)
    n = max(a_s)
    largest = n
    if n // 2 in a_s and n // 3 in a_s and n // 5 in a_s:
        largest = n // 2 + n // 3 + n // 5
    m = []
    for _ in range(3):
        if not a_s:
            break
        n = max(a_s)
        a_s = set([j for j in a_s if n % j != 0])
        m.append(n)
        if sum(m) > largest:
            largest = sum(m)
    return largest


q = int(input())

for _ in range(q):
    n = int(input())
    a_s = list(map(int, input().split()))
    print(solve(a_s))
