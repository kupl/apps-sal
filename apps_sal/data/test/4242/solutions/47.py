A, B, K = map(int, input().split())
m = min(A, B)
l = []
for i in range(1, m + 1):
    if A % i == 0 and B % i == 0: l.append(i)
print(l[-K])
