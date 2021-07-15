n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
for i in range(n-m+1):
    for j in range(n-m+1):
        ans = True
        for k in range(m):
            if b[k] != a[i+k][j:j+m]:
                ans = False
        if ans:
            print("Yes")
            return
print("No")
