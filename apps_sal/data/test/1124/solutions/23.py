n = int(input())
a = set(list(map(int, input().split())))


def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


ans = min(a)
for i in a:
    ans = gcd(i, ans)
print(ans)
