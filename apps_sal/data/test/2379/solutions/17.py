N, K, C = map(int, input().split())
S = input()

l = [0] * K
i = 0
for j in range(K):
    while S[i] == "x":
        i += 1
    l[j] = i
    i += C + 1

r = [0] * K
i = N - 1
for j in range(K - 1, -1, -1):
    while S[i] == "x":
        i -= 1
    r[j] = i
    i -= C + 1
# print(l, r)
[print(l_i + 1) for l_i, r_i in zip(l, r) if l_i == r_i]
