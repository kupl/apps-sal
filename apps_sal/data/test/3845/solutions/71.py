(A, B) = map(int, input().split())
h = 96
w = 99
S = [['.' for _ in range(w)] for _ in range(h)]
for i in range(48, h):
    for j in range(w):
        S[i][j] = '#'
cnt = 0
while cnt < B - 1:
    for i in range(16):
        for j in range(33):
            S[3 * i + 1][3 * j + 1] = '#'
            cnt += 1
            if cnt == B - 1:
                break
        if cnt == B - 1:
            break
    if cnt == B - 1:
        break
cnt = 0
while cnt < A - 1:
    for i in range(16):
        for j in range(33):
            S[48 + 3 * i + 1][3 * j + 1] = '.'
            cnt += 1
            if cnt == A - 1:
                break
        if cnt == A - 1:
            break
    if cnt == A - 1:
        break
print(h, w)
for i in range(h):
    print(''.join(S[i]))
