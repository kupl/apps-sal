N=int(input())
lst = [int(n) for n in input().split()]
m=999999
cnt = 0
for l in range(N):
    m = min(m,lst[l])
    if m==lst[l]:
        cnt+=1
print(cnt)

