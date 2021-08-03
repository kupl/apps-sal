ans = 1
flag = False
n = int(input())
while n % 2 == 0:
    if flag == False:
        flag = True
        ans *= 2
    n = n // 2
flag = False
i = 3
while i * i <= n:
    while n % i == 0:
        if flag == False:
            flag = True
            ans *= i
        n = n // i
    flag = False
    i += 2
if n > 2:
    ans *= n
print(ans)
