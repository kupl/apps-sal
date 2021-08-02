n = int(input())
p = [int(x) for x in input().split()]

ans = 0
cnt = 0
'''
index = 0
while index <= n-1:
    if p[index] == index+1:
        if p[index+1] != index+2:
            index += 1
        else:
            index += 2
        ans += 1
    else:
        index += 1
'''

for i in range(n - 1):
    if p[i] == i + 1:
        p[i], p[i + 1] = p[i + 1], p[i]
        cnt += 1

if p[-1] == n:
    cnt += 1

print(cnt)
