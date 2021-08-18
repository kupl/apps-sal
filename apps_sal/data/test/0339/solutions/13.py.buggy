n = int(input())
k = int(input())
a = int(input())
b = int(input())
x = n
cost = 0

if k == 1:
    print(int((x - 1) * a))
    return

while x > 1:
    if x < k:
        cost += (x - 1) * a
        break
    rem = x % k
    x -= rem
    cost += a * rem
    if rem == 0:
        temp = (x // k) * (k - 1)
        x //= k
        cost += min(temp * a, b)

print(cost)
