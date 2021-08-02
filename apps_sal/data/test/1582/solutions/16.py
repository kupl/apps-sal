N = int(input())
A = [[0 for j in range(9)] for i in range(9)]
count = 0
for x in range(1, N + 1):
    if x % 10 == 0:
        continue
    if x >= 10**(count + 1):
        count += 1
    i = x % 10
    j = x // (10**count)
    A[i - 1][j - 1] += 1
ans = 0
for i in range(9):
    for j in range(i, 9):
        r = 2 if i != j else 1
        ans += A[i][j] * A[j][i] * r

print(ans)
# for a in A:
#  print(a)
