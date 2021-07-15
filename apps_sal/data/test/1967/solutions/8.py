
w, h = list(map(int, input().split()))
first_matr = list()
second_matr = [' '] * w
for i in range(w):
    second_matr[i] = [' '] * h

third_matr = [' '] * 2 * w
for i in range(2 * w):
    third_matr[i] = [' '] * 2 * h

for i in range(h):
    s = input()
    first_matr.append([])
    for j in s:
        first_matr[i].append(j)

for i in range(w):
    for j in range(h):
        second_matr[i][j] = first_matr[j][i]

for i in range(w):
    for j in range(h):
        third_matr[2*i][2*j] = third_matr[2*i+1][2*j] = third_matr[2*i][2*j+1] = third_matr[2*i+1][2*j+1] = second_matr[i][j]

for k in third_matr:
    for j in k:
        print(j, end="")
    print()

