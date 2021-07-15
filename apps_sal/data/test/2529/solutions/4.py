# cook your dish here
req, total = map(float, input().split())
ans = total
if req >= total:
    ans = total
elif req % 5 != 0:
    ans = total
else:
    ans = total - req - 0.5
ans = total if ans < 0 else ans 
print(ans)
