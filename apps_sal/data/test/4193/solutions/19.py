A = [list(map(int, input().split())) for _ in range(3)]
for j in range(3): A.append([A[i][j] for i in range(3)])
A.append([A[0][0], A[1][1], A[2][2]])
A.append([A[2][0], A[1][1], A[0][2]])
d = {int(input()): 0 for _ in range(int(input()))}
print("YNeos"[all(any(d.get(v, 1) for v in r) for r in A)::2])
