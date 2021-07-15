m = 1000000007
input()
n, d = 2, 1
for q in map(int, input().split()): d, n = q & d, pow(n, q, m)
n = n * pow(2, m - 2, m) % m
k = (n + 1 - 2 * d) * pow(3, m - 2, m) % m
print(str(k) + '/' + str(n))
