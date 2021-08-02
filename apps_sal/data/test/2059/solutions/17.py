N = int(input())
a = list(map(int, input().split()))
ans = 10**10
a0 = a[0]
for i in range(N - 1):

    ans = min(ans, (min(a0, a[i + 1])) // (i + 1))

ar = a[-1]
for i in range(N - 1):
    ans = min(ans, (min(ar, a[i])) // (N - i - 1))
print(ans)
