x = int(input())

ans = 1
for i in range(2, int(x**(1/2)//1+1)):
    v = 1
    while v*i <= x:
        v *= i
    ans = max(ans, v)
print(ans)
