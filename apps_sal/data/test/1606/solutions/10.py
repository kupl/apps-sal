from sys import stdin
input = stdin.readline

n = int(input())
l = list(list(map(int, input().split())) for _ in range(n))
q = int(input())
output = []
ans = 0


for i in range(n):
    ans ^= l[i][i]

for i in range(q):
    command = input()
    if command[0] == '3':
        output.append(ans)
    else:
        ans ^= 1

print(''.join([*map(str, output)]))
