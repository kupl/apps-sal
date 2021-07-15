n = int(input())

num = n + 1
k = 0

high = n + 1
low = 1
while n > 0:
    n = (low + high) // 2
    temp = n * (n + 1) // 2
    if temp <= num:
        if low == n and low <= high:
          break
        low = n
    else:
        if high == n and high >= low:
          break
        high = n

# print(low)
# print(high)
n = (low + high) // 2
# print(n)
print(num - n)
