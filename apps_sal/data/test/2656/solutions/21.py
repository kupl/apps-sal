K = int(input())
S = input()
m = 1000000007
result = 0
t = pow(26, K, m)
u = pow(26, -1, m) * 25 % m
l = len(S)
for i in range(K + 1):
    result = (result + t) % m
    t = t * u % m * (l + i) % m * pow(i + 1, -1, m) % m
print(result)
