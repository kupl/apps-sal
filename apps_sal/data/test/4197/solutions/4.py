n = int(input())
a_l = list(map(int, input().split()))
ans = [0] * n 
for i, a in enumerate(a_l):
    ans[a-1] = i+1
print(*ans)
