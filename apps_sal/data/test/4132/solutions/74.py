def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


n = int(input())
l = list(map(int, input().split()))
l.sort()
tmp = gcd(l[0], l[1])
for i in range(2, len(l)):
    tmp = gcd(tmp, l[i])
print(tmp)
