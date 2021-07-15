# arc109b
n = int(input())

# x(x+1)/2 <= n+1
# x <= (-1+sqrt(8n+9))/2

MX = 2 * (10 ** 9)
l = 0
r = MX
while r - l > 1:
    mid = (r+l)//2
    if mid * (mid + 1) <= 2 * (n+1):
        l = mid
    else:
        r = mid
print(n + 1 - l)
