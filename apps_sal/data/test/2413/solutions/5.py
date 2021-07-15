def solve():
    n = int(input())
    s = input()
    mn = mx = None
    for i in range(n):
        if s[i] == '0':
            continue
        if mn is None or mn > i:
            mn = i
        if mx is None or mx < i:
            mx = i
    ans = n
    if mn is not None:
        ans = max(ans, (n - mn) * 2)
    if mx is not None:
        ans = max(ans, (1 + mx) * 2)
    print(ans)


def main():
    t = int(input())
    for _ in range(t):
        solve()


main()

