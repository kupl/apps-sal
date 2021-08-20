n = int(input())
A = [0] * 5
B = [0] * 5
for a in map(int, input().split()):
    A[a - 1] += 1
for a in map(int, input().split()):
    B[a - 1] += 1
if any([(x + y) % 2 != 0 for (x, y) in zip(A, B)]):
    print(-1)
else:
    print(sum([abs(x - y) // 2 for (x, y) in zip(A, B)]) // 2)
