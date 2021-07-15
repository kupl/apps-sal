def d(x):
    c = 0
    while x > 0:
        c += x%10
        x //= 10
    return c
n = int(input())
ans = 0
if n <= 10:
    ans = n
else:
    temp = 9
    while temp*10+9 < n:
        temp *= 10
        temp += 9
    b = n - temp
    ans += d(b)
    ans += d(temp)
print(ans)
