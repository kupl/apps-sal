n = int(input())
c = input()
a = c.count('R')
cnt = 0
for i in range(a):
    if c[i] == 'W':
        cnt += 1
print(cnt)
