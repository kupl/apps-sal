def sum(n):
    ans = 0
    while n > 0:
        ans += (n % 10)
        n = n // 10
    return ans


n = int(input())
if n > 5000:
    temp = 2000017
    count = 5000
else:
    temp = 28
    count = 1
while count != n:
    if sum(temp) == 10:
        count += 1
    temp += 9
print(temp - 9)
