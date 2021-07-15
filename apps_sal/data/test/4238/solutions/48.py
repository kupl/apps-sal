n = list(map(int,input().split()))
ans = "Yes"
if sum(n)%9:
    ans = "No"
print(ans)
