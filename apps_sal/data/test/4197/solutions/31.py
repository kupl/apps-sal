n = int(input())
line = list(map(int, input().split()))
ans = ['0' for i in range(n)]
for i in range(n):
    ans[line[i] - 1] = str(i + 1)
print(' '.join(ans))
