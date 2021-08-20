n = int(input())
num = n + 1
k = 0
high = n + 1
low = 1
while n > 0:
    n = (low + high) // 2
    temp = n * (n + 1) // 2
    if temp <= num:
        if low == n:
            break
        low = n
    else:
        if high == n:
            break
        high = n
n = (low + high) // 2
print(num - n)
