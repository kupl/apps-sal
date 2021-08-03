import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

B = []
for i in range(n):
    for j in range(i + 1, n):
        if A[i] > A[j]:
            B.append((A[i], i + 1, j + 1))

B.sort()
B.sort(reverse=True, key=lambda x: x[2])

print(len(B))
for x, y, z in B:
    print(y, z)
