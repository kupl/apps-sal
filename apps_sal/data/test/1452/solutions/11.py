modus = 1000000007

R, C = map(int, input().split())

r_lst = list(map(int, input().split()))
c_lst = list(map(int, input().split()))

M = [[-1 for j in range(C)] for i in range(R)]

impossible = False
for i, r in enumerate(r_lst):

    for index in range(r):
        M[i][index] = 1

    if r != C:
        M[i][r] = 0

for i, c in enumerate(c_lst):

    for index in range(c):
        if M[index][i] == 0:
            impossible = True
            break

        M[index][i] = 1

    if impossible:
        break

    if c != R:

        if M[c][i] == 1:
            impossible = True
            break

        M[c][i] = 0

if impossible:
    print(0)
else:
    count = 0
    for i in range(R):
        for j in range(C):
            if M[i][j] == -1:
                count += 1

    result = pow(2, count, modus)
    print(result)
