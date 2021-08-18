import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, l = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a = [0] + a + [l]

    s = [0 for i in range(n + 2)]
    e = [0 for i in range(n + 2)]
    for i in range(1, n + 2):
        s[i] = (a[i] - a[i - 1]) / i
        s[i] += s[i - 1]
    a = a[::-1]
    for i in range(1, n + 2):
        e[i] = (a[i - 1] - a[i]) / i
        e[i] += e[i - 1]
    e = e[::-1]
    a = a[::-1]

    for i in range(1, n + 2):
        if s[i] >= e[i]:
            s_speed = i
            e_spped = n + 2 - i
            if s[i - 1] <= e[i]:
                L = a[i] - a[i - 1] - s_speed * (e[i] - s[i - 1])
                t = L / (n + 2)
                ans = e[i] + t
                print(ans)
                break
            else:
                L = a[i] - a[i - 1] - e_spped * (s[i - 1] - e[i])
                t = L / (n + 2)
                ans = s[i - 1] + t
                print(ans)
                break
