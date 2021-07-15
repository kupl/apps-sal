import copy
n = int(input())
li = list(map(int,input().split()))
li1 = copy.copy(li)
li1.sort()
cnt = 0
for i in range(n):
    if li[i] != li1[i]:
        cnt += 1

if cnt <= 2:
    print('YES')
else:
    print('NO')
