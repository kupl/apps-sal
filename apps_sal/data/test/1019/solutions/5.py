n = int(input())


def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


ans = None
for i in range(n):
    if i >= n - i:
        break
    if gcd(i, n - i) == 1:
        ans = [i, n - i]
print(ans[0], ans[1])
