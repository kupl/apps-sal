n = int(input())
d = int(input())
e = int(input())
e *= 5
dollar = 0
ans = n
while d * dollar <= n:
    val = n - d * dollar
    ans = min(ans, val % e)
    dollar += 1
print(ans)
