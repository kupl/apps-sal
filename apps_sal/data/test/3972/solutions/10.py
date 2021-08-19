mod = 10**9 + 7

N = int(input())

X = [1, 1, 1]
Y = [1, 2, 3]
for i in range(3, N + 2):
    x = (X[-1] + Y[i - 3]) % mod
    X.append(x)
    Y.append((Y[-1] + x) % mod)

ans = ((Y[N - 2] * (N - 2) + (Y[N - 1])) * (N - 1) + (N - 1) * Y[N - 2] + 1) % mod
print(ans)


# from itertools import product

# A = product(range(1, N+1), repeat=N)
# P = []
# for B in A:
#     ok = True
#     B = list(B) + [B[-1]]*(N+1)
#     for i in range(N):
#         b = B[i]
#         if len(set(B[i+1:i+1+b])) != 1:
#             ok = False
#             break
#     if ok:
#         P.append(B)
# print(len(P))
# for B in P:
#     print(B)
