s = input()
n = len(s)

lis = [0]*n

r = 0
l = 0
for i in range(n):
    r += 1
    if s[i] == 'L':
        lis[i-1] += r//2
        lis[i] += (r+1)//2
        r = 0

for j in range(n-1, -1, -1):
    l += 1
    if s[j] == 'R':
        lis[j+1] += l//2
        lis[j] += (l+1)//2
        l = 0
    lis[j] -= 1

print(*lis)
