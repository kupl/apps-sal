import math
n = int(input())
a_list = list(map(int, input().split()))
gcd = a_list[0]
for i in range(1, n):
    gcd = math.gcd(gcd, a_list[i])


print(gcd)
