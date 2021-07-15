n, m = [int(x) for x in input().split()]
books = [int(x) for x in input().split()]
D = {i:0 for i in range(1,m+1)}
for i in range(n):
    D[books[i]] += 1

res = 0
for k in D:
    res += D[k] * (n - D[k])

print(res // 2)

