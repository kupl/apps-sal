n, h, k = map(int, input().split())
a = list(map(int, input().split()))[::-1]
ans = b = 0
while a != []:
    while len(a) and b + a[-1] <= h:
        b = b + a.pop()
    if b // k == 0:
        ans, b = ans + 1, 0
    else:
        ans, b = ans + b // k, b % k
print(ans + (b > 0))
