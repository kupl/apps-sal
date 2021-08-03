import itertools

N = int(input())
A = []
for n in range(N):
    x, y = map(int, input().split())
    A.append((x, y))

pattern = itertools.permutations(A, N)
temp = 0
number = 0
for i in pattern:
    number += 1
    for j in range(len(i) - 1):
        temp += ((i[j][0] - i[j + 1][0])**2 + (i[j][1] - i[j + 1][1])**2)**0.5

print(temp / number)
