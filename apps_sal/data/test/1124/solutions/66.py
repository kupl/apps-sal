n = int(input())

i = list(map(int, input().split()))
ans = i[0]


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


for k in range(1, n):
    ans = gcd(ans, i[k])
print(ans)
