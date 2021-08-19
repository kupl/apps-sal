n = int(input())
fib = [1, 2]
for i in range(2, 10000):
    fib.append(fib[i - 1] + fib[i - 2])
l = 0
r = 10000
while r - l > 1:
    mid = (r + l) // 2
    if fib[mid] > n:
        r = mid
    else:
        l = mid
print(l)
