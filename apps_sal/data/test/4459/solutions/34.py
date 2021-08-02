N = int(input())

a = list(map(int, input().split()))

a.sort()
c = 1
ans = 0
for i in range(N - 1):
    if a[i] == a[i + 1]:
        c += 1
        if c > a[i]:
            ans += 1
    else:
        if c < a[i]:
            ans += c
            c = 1
        else:
            c = 1
if c < a[N - 1]:
    ans += c

print(ans)
