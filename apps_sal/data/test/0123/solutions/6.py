(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = list(reversed(sorted(b)))
j = 0
for i in range(n):
    if a[i] == 0:
        a[i] = b[j]
        j += 1
ans = 'No'
for i in range(n - 1):
    if a[i] >= a[i + 1]:
        ans = 'Yes'
        break
print(ans)
