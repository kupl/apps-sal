N = int(input())
a = list(map(int, input().split()))
a.sort()
ans = []
for n in range(N):
    r = n // 2
    if n % 2 == 0:
        x = a[r]
    else:
        x = a[N - 1 - r]
    ans.append(x)
print(' '.join(map(str, ans)))
