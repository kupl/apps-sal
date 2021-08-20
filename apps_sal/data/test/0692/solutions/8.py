def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


n = int(input())
m = list(map(int, input().split()))
r = list(map(int, input().split()))
cap = 1
for val in m:
    cap = lcm(cap, val)
ans = 0
for day in range(cap):
    works = False
    for i in range(n):
        if day % m[i] == r[i]:
            works = True
            break
    if works:
        ans += 1
print(ans / cap)
