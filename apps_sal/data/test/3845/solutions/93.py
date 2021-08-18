A, B = list(map(int, input().split()))
h, w = 99, 99

a = '.'
b = '

if A > B:
    a, b = b, a
    B, A = A, B
A -= 1
ANS = [[b] * w for i in range(h)]
B -= 1
idx = 0

for i in range(w):
    ANS[0][i] = a
for i in range(49):
    ANS[i][0] = a
    ANS[i][-1] = a
while(B):
    idx += 1
    for i in range(1, w, 2):
        if B == 0:
            ANS[idx][i] = a
            ANS[idx][i + 1] = a
        else:
            ANS[idx][i] = b
            ANS[idx][i + 1] = a
            B -= 1
    idx += 1
    for i in range(w):
        ANS[idx][i] = a
idx += 1


for i in range(idx, 49):
    for j in range(w):
        ANS[i][j] = a

for i in range(w):
    ANS[49][i] = b
for i in range(49, h):
    ANS[i][0] = b
    ANS[i][-1] = b
idx = 49
while(A):
    idx += 1
    for i in range(1, w, 2):
        if A == 0:
            ANS[idx][i] = b
            ANS[idx][i + 1] = b
        else:
            ANS[idx][i] = a
            ANS[idx][i + 1] = b
            A -= 1
    idx += 1
    for i in range(w):
        ANS[idx][i] = b

for i in range(idx, h):
    for j in range(w):
        ANS[i][j] = b

print((h, w))

for i in range(h):
    print(("".join(ANS[i])))
