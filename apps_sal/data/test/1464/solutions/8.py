n = int(input())
all = set()
for w in range(n):
    s = input()
    for i in range(len(s) + 1):
        for j in range(i):
            all.add(s[j:i])
cnt = 0
limit = 26
l = 1
while True:
    s = ''
    tmp = cnt
    for i in range(l):
        s = chr(ord('a') + tmp % 26) + s
        tmp //= 26
    if s not in all:
        print(s)
        break
    cnt += 1
    if cnt == limit:
        cnt = 0
        limit *= 26
        l += 1
