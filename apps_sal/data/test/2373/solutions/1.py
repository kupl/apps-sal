n = int(input())
p = [int(x) for x in input().split()]
ans = 0
cnt = 0
'\nindex = 0\nwhile index <= n-1:\n    if p[index] == index+1:\n        if p[index+1] != index+2:\n            index += 1\n        else:\n            index += 2\n        ans += 1\n    else:\n        index += 1\n'
for i in range(n - 1):
    if p[i] == i + 1:
        (p[i], p[i + 1]) = (p[i + 1], p[i])
        cnt += 1
if p[-1] == n:
    cnt += 1
print(cnt)
