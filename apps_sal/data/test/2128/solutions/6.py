
M = 998244353

n = int(input())

exp = 0
for pi in map(int, input().split()):
    exp = (exp + 1) * 100 * pow(pi, M - 2, M) % M

print(exp)
