N = int(input())
K = int(input())

a = 1
for _ in range(N):
    if a*2 < a+K:
        a *= 2
    else:
        a += K
print(a)
