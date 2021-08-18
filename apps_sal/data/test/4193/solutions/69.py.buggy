A = [[], [], []]
A[0] = [int(s) for s in input().split(' ')]
A[1] = [int(s) for s in input().split(' ')]
A[2] = [int(s) for s in input().split(' ')]
N = int(input())
B = []
for n in range(N):
    b = int(input())
    B.append(b)
B = set(B)
lines = []
lines.append(set(A[0]))
lines.append(set(A[1]))
lines.append(set(A[2]))
lines.append(set(A[i][i] for i in range(3)))
lines.append(set(A[2 - i][i] for i in range(3)))
lines.append(set(A[i][0] for i in range(3)))
lines.append(set(A[i][1] for i in range(3)))
lines.append(set(A[i][2] for i in range(3)))
for line in lines:
    if len(line & B) == 3:
        print('Yes')
        return
print('No')
