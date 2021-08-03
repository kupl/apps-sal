def f(x):
    nonlocal a
    if len(ans) == n:
        print(' '.join(map(str, ans)))
        return
    if x % 3 == 0 and x // 3 in a:
        ans.append(x // 3)
        f(x // 3)
        ans.pop()
    if x * 2 in a:
        ans.append(x * 2)
        f(x * 2)
        ans.pop()


n = int(input())
a = list(map(int, input().split()))

ans = []
for i in range(n):
    ans.append(a[i])
    f(a[i])
    ans.pop()
