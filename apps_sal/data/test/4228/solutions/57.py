N, L = map(int, input().split())

T = [L+i for i in range(N)]

if T[-1] >= 0:
    m = min((i for i in T if i >= 0))
else:
    m = T[-1]

print(sum(T)-m)
