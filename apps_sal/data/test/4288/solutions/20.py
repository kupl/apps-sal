lst = input().split()
a = int(lst[0])
b = int(lst[1])
c = int(lst[2])
cnt = 0
if a == b:
    cnt += 1
if b == c:
    cnt += 1
if c == a:
    cnt += 1
if cnt == 1:
    print('Yes')
else:
    print('No')
