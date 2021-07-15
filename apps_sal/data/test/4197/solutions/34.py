n = int(input())
a = list(map(int,input().split()))
ans = [0] * n
for i,j in enumerate(a):
    ans[j-1] = i + 1
print(*ans)
