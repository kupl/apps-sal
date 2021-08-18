
N, K, C = map(int, input().split())
S = input()

l = []
num = 0
i = 0
while num < K:
    if S[i] == "o":
        l.append(i)
        num += 1
        i += C + 1
    else:
        i += 1

r = []
num = 0
i = N - 1
while num < K:
    if S[i] == "o":
        r.append(i)
        num += 1
        i -= C + 1
    else:
        i -= 1
r.reverse()

for i in range(K):
    if l[i] == r[i]:
        print(l[i] + 1)
