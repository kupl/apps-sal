(A, B) = map(int, input().split())
T = [['.' for _ in range(100)] for _ in range(100)]
for i in range(50, 100):
    for j in range(100):
        T[i][j] = '#'
cnt = 1
if B > 1:
    flag = 0
    for i in range(1, 49, 2):
        for j in range(1, 100, 2):
            T[i][j] = '#'
            cnt += 1
            if cnt == B:
                flag = 1
                break
        if flag == 1:
            break
cnt = 1
if A > 1:
    flag = 0
    for i in range(51, 99, 2):
        for j in range(1, 100, 2):
            T[i][j] = '.'
            cnt += 1
            if cnt == A:
                flag = 1
                break
        if flag == 1:
            break
print(100, 100)
for i in range(100):
    print(''.join(T[i]))
