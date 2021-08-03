n, m = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(n)]
count = 4
for i in range(m):
    if A[0][i] == 1 or A[-1][i] == 1:
        count = 2
for i in range(n):
    if A[i][0] == 1 or A[i][-1] == 1:
        count = 2
print(count)
