x,y = map(lambda x: int(x,16),input().split())
ans = "="
if x < y: ans = "<"
elif x > y: ans = ">"
print(ans)
