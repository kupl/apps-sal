A = ['RGB', 'RBG', 'BRG', 'BGR', 'GRB', 'GBR']
n = int(input())
s = input()
ans = n + 1
f = 0
for i in range(6):
    k = 0
    for j in range(n):
        if s[j] != A[i][j % 3]:
            k += 1
    if k < ans:
        ans = k
        f = i
print(ans)
for i in range(n):
    print(A[f][i % 3], end='')
