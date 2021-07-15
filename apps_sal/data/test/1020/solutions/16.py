n, m, k = map(int, input().split())
x = n
ans = 0
for i in range(k):
    ans+= 2*x
    x -= 4
x = m
for i in range(k):
    ans+= 2*x
    x -= 4
ans -= k*4

print(ans)
