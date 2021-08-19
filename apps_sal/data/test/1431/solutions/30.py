n = int(input())
a = list(map(int, input().split()))
ans = [0 for _ in range(n + 1)]
t = []
S = 0
for i in range(n):
    b = n - i
    c = (n - i) * 2
    ch = 0
    while c <= n:
        ch += ans[c]
        c += b
    if ch % 2 == 0:
        if a[b - 1] == 1:
            ans[b] += 1
            S += 1
            t.append(str(b))
    elif a[b - 1] == 0:
        ans[b] += 1
        S += 1
        t.append(str(b))
print(S)
if S > 0:
    print(' '.join(t))
