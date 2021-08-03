N = int(input())
K = int(input())
res = 1
for i in range(N):
    if res * 2 <= res + K:
        res *= 2
    else:
        res += K
print(res)
