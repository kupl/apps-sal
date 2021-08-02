from sys import stdin
input = stdin.readline
n = int(input())
lis = list(list(map(int, input().split())) for _ in range(n))
u = 0
for i in range(n):
    for j in range(n):
        if i == j:
            u ^= lis[i][j]
ans = []
k = int(input())
for i in range(k):
    s = input()
    if s[0] == '3':
        ans.append(str(u))
    else:
        u ^= 1
print(''.join(ans))
