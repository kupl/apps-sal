from itertools import accumulate
N = int(input())

T = [0] * (N + 1)

for i, j in enumerate(map(int, input().split())):
    j -= 1
    if i > j:
        i, j = j, i
    T[i] += 1
    T[j] -= 1

T = list(accumulate(T))
T.pop()


for i, j in zip(map(int, input()), T):
    if j != 0 and i == 0:
        print('NO')
        return

print('YES')
