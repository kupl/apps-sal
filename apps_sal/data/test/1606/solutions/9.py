from sys import stdin
input = stdin.readline
n = int(input())
lis = list(list(map(int, input().split())) for _ in range(n))
val = 0
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += lis[i][j] * lis[j][i]
    val += tmp % 2
val = val % 2
q = int(input())
ans = []
for i in range(q):
    ss = input()
    if ss[0] == '3':
        ans.append(str(val))
    else:
        val = val ^ 1
print(''.join(ans))
