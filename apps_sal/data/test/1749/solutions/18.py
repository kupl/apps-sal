(n, l, r) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 'TRUTH'
for i in range(0, l - 1):
    if a[i] != b[i]:
        ans = 'LIE'
        break
for i in range(r, n):
    if a[i] != b[i]:
        ans = 'LIE'
        break
print(ans)
