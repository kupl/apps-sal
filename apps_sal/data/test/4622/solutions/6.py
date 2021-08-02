N = int(input())
A = sorted(list(map(int, input().split())))
l = []
# print(A)
for i in range(N - 1):
    l.append(A[i + 1] - A[i])

if 0 in l:
    print('NO')
else: print('YES')
