N = int(input())
p = list(map(int,input().split()))

s_p = sorted(p)

cnt = 0
for i in range(N):
    if p[i] != s_p[i]:
        cnt += 1

if cnt > 2:
    print("NO")
else:
    print("YES")
