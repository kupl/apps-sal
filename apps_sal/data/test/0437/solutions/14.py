n = int(input())

ans = 0
for i in range(n):
    i = n-i
    ans += 1 / i

print (ans)

