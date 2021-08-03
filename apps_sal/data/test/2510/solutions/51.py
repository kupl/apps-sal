N, M = list(map(int, input().split()))
A = [0] * M
B = [0] * M
R = [0] * N
for i in range(N):
    R[i] = set()

for i in range(M):
    A[i], B[i] = list(map(int, input().split()))
    R[A[i] - 1].add(B[i] - 1)
    R[B[i] - 1].add(A[i] - 1)

stack = set()
visited = set()
max_groups = 0

for i in range(N):
    if not i in visited:
        stack.add(i)
        groups = 0
        while True:
            current = stack.pop()
            visited.add(current)
            groups += 1
            stack |= (R[current] - visited)
            if not stack:
                break
        max_groups = max(max_groups, groups)

print(max_groups)
