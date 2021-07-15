n = int(input())
A = list(map(int,input().split()))
if not 1 in A:
    print((-1))
    return
num = 1
cnt = 0
for a in A:
    if a == num:
        num += 1
    else:
        cnt += 1
print(cnt)

