def sum_digits3(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r

n = int(input())
ans=10
for i in range(n):
    while(True):
        ans+=9
        if sum_digits3(ans)==10:
            break
print(ans)

