from fractions import gcd
n = int(input())
l = list(map(int, input().split()))
ans = 0
new = [l[0]]
for i in range(1, n):
    if gcd(l[i], l[i - 1]) != 1:
        ans += 1
        new.append(1)
    new.append(l[i])
print(ans)
print(*new)
