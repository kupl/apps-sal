N = int(input())
alist = list(map(int, input().split()))
alist.sort()
ans = 0
for i in range(N*2):
    if i%2==0:
        ans += alist[i]
print(ans)
