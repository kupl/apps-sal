def f(n):
    d = 2
    A = []
    while d * d <= n:
        if n % d == 0:
            A.append(d)
            n = n // d
            
        else:
            d += 1
    if n != 1:
        A.append(n)
    return A

n = int(input())
a, b = map(int, input().split())
A = set(f(a))
B = set(f(b))
ans = A.union(B)
ans = list(ans)
for i in range(1, n):
    a, b = map(int, input().split())
    upd = ans.copy()
    for j in ans:
        if a % j != 0 and b % j != 0:
            upd.remove(j)
    ans = upd.copy()

if len(ans) == 0:
    print(-1)
else:
    print(ans[0])
