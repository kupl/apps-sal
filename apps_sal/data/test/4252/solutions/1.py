n = int(input())
s = input() + ' '*(n%3)
cnt = 0

for x in range(n):
    if s[x:x+3] == 'xxx':
        cnt += 1

print(cnt)
