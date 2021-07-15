from collections import Counter


def binomial_coefficient(n, r):
    res = 1
    for i in range(r):
        res *= (n - i)
        res //= (i + 1)
    return res


N, A, B = list(map(int, input().split()))
V = list(map(int, input().split()))
V.sort(reverse=True)

C = Counter(V)

ave = sum(V[:A]) / A
num = V[A - 1]
Nnums = C[num]

if num == V[0]:
    B = min(B, Nnums)
    cnt = 0
    for i in range(A, B + 1):
        cnt += binomial_coefficient(Nnums, i)
else:
    for k, v in list(C.items()):
        if k > num:
            A -= v
    cnt = binomial_coefficient(Nnums, A)

print(ave)
print(cnt)

