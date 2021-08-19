n = int(input())
f = input().split(' ')
pos = [0 for i in range(n)]
for i in range(n):
    pos[int(f[i]) - 1] = i
ret = 0
for i in range(n - 1):
    ret += abs(pos[i + 1] - pos[i])
print(ret)
