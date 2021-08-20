(A, B) = map(int, input().split())
T = [['.' for _ in range(100)] for _ in range(100)]
for i in range(50, 100):
    for j in range(100):
        T[i][j] = '#'
cnt = 1
for i in range(1, 48, 2):
    for j in range(1, 100, 2):
        if cnt < B:
            T[i][j] = '#'
            cnt += 1
cnt = 1
for i in range(51, 100, 2):
    for j in range(1, 100, 2):
        if cnt < A:
            T[i][j] = '.'
            cnt += 1
print(100, 100)
for i in range(100):
    print(''.join(T[i]))
