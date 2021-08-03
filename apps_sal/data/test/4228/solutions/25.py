N, L = map(int, input().split())
s = N * L
for i in range(N + 1):
    s += i
s -= N
K = []
for i in range(1, N + 1):
    K.append(L + i - 1)
if 0 <= K[0]:
    s -= K[0]
elif K[0] < 0 and K[N - 1] > 0:
    s = s
else:
    s -= K[N - 1]
print(s)
