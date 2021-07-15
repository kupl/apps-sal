n, x, y = map(int, input().split())
a = [0]*(n-1)
for i in range(1, n):
    for j in range(i+1, n+1):
        b = min(j-i, abs(x-i)+1+abs(y-j))
        a[b-1] += 1
print(*a, sep="\n")
