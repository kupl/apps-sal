n = int(input())
s = input()
cnt = 0
num = 0
chk = False
for i in range(n):
    if chk and s[i] == 'L':
        if cnt % 2 == 1:
            num += 1
        chk = False
        continue
    if s[i] == 'R':
        chk = True
        cnt = 0
        continue
    if chk:
        cnt += 1
        continue
    if s[i] == 'L':
        num = 0
    else:
        num += 1
print(num)
