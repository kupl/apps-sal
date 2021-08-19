(h, w) = map(int, input().split())
A = [list(input()) for i in range(h)]
answ = []
ansh = []
for i in range(h):
    if not all([a == '.' for a in A[i]]):
        answ.append(i)
for j in range(w):
    if not all([A[i][j] == '.' for i in range(h)]):
        ansh.append(j)
for i in answ:
    for j in ansh:
        print(A[i][j], end='')
    print('')
