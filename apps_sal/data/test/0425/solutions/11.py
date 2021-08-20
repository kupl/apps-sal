(n, p) = map(int, input().split())
ans = -1
for i in range(10001):
    if n - i * p >= i:
        c = bin(n - i * p)[2:].count('1')
        if c <= i:
            ans = i
            break
print(ans)
