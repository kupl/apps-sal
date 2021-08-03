n = input()
lessons = input().split()
prev = '0'
home = True
cnt = 0
for l in lessons:
    if l == '0' and prev == '0':
        home = True
    elif l == '1':
        cnt += 1
        if prev == '0' and not home:
            cnt += 1
        home = False
    prev = l
print(cnt)
