(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = []
for i in range(n):
    for j in range(m):
        if a[i] != b[j]:
            ans.append(a[i] * 10 + b[j])
            ans.append(a[i] + b[j] * 10)
        else:
            ans.append(a[i])
print(min(ans))
