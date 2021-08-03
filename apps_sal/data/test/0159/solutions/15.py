n = int(input())
l = list(map(int, input().split()))
ans = [str(l[0])]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


for i in range(1, n):
    if gcd(l[i], l[i - 1]) > 1:
        ans += ["1"]
    ans += [str(l[i])]
print(len(ans) - n)
print(' '.join(ans))
