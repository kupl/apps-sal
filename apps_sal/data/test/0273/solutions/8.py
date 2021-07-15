a, b = input().split()
ans = a[0]
for i in range(1, len(a)):
    if a[i] < b[0]:
        ans += a[i]
    else:
        break
ans += b[0]
print(ans)
