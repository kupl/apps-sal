
def rint():
    return int(input())


def rints():
    return list(map(int, input().split()))


t = rint()
for _ in range(t):
    n = rint()
    s = input()
    mx = n
    for i in range(n):
        if s[i] == '0':
            continue
        mx = max(mx, 2 * max(i + 1, n - i))
    print(mx)
