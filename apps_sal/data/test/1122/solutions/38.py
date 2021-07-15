n, m = list(map(int, input().split()))
ans = []
if n % 2 == 1:
    for i in range(m):
        ans.append((i+1, n-i))


else:
    for i in range(m):
        if i <= (m+1)//2-1:
            ans.append((i+1, n-i))
        else:
            ans.append((i+1, n-i-1))

for a, b in ans:
    print((a, b))

