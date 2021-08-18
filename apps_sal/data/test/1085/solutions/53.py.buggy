n = int(input())

if n == 2:
    print(1)
    return
num = n - 1
cnt = 1
lst = [n]
for i in range(2, int(n ** 0.5) + 1):
    if num % i == 0:
        cnt += 2
        if num == i ** 2:
            cnt -= 1
    if n % i == 0:
        lst.append(i)
        if n != i ** 2:
            lst.append(n // i)
for num in lst:
    n2 = n
    while n2 % num == 0:
        n2 //= num
    if n2 % num == 1:
        cnt += 1
print(cnt)
