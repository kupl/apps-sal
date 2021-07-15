N, K, C = list(map(int, input().split()))
S = input()

s = []

count = 0
for i in range(N):
    if len(s) == K:
        break
    if count == 0:
        if S[i] == 'x':
            continue
        else:
            count = C
            s.append(i+1)
    else:
        count -= 1
s2 = []
count = 0
for i in range(N-1, -1, -1):
    if len(s2) == K:
        break
    if count == 0:
        if S[i] == 'x':
            continue
        else:
            s2.append(i+1)
            count = C
    else:
        count -= 1

for a, b in zip(s, s2[::-1]):
    if a == b:
        print(a)

