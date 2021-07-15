N = int(input())
p = list(map(int,input().split()))
cnt = 0
bol = 0
for i in range(N-1):
    if bol == 1:
        bol = 0
        continue
    if p[i] == i+1 and p[i+1] == i+2:
        cnt += 1
        bol = 1
    elif p[i] == i+1:
        cnt += 1
if bol == 0 and p[N-1] == N:
    cnt += 1
print(cnt)
