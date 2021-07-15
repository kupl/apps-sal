N = int(input())
ans = 'No'
cnt = 0
for _ in range(N):
    d1,d2 = input().split()
    if d1 == d2:
        cnt += 1
        if cnt == 3:
            break
    else:
        cnt = 0
if cnt == 3:
    ans = 'Yes'
print(ans)
