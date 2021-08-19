N = int(input())
count = 0
flag = 0
for i in range(N):
    (a, b) = list(map(int, input().split()))
    if a == b:
        count += 1
    else:
        count = 0
    if count == 3:
        flag = 1
if flag == 1:
    print('Yes')
else:
    print('No')
