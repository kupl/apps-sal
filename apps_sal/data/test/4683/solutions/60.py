p = 10 ** 9 + 7
n = int(input())
aa = list(map(int, input().split()))
s = 0
for a in aa:
    s += a ** 2
sa = sum(aa)
b = sa * sa
ans = (b - s) // 2
print(ans % p)
