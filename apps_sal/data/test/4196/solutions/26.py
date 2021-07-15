from math import gcd
n = int(input())
alst = list(map(int, input().split()))
l_gcd = [alst[0]]
for num in alst[1:-1]:
    l_gcd.append(gcd(l_gcd[-1], num))

r_gcd = [alst[-1]]
for num in alst[1:-1][::-1]:
    r_gcd.append(gcd(r_gcd[-1], num))
r_gcd = r_gcd[::-1]
ans = max(r_gcd[0], l_gcd[-1])


for num1, num2 in zip(r_gcd[1:], l_gcd[:-1]):
    tmp = gcd(num1, num2)
    ans = max(ans, tmp)
print(ans)
