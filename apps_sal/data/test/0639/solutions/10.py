n,x = map(int, input().split())
a=set(list(map(int, input().split())))
ans = 0
for i in range(x):
     if i not in a:
            ans += 1
if x in a:
    ans += 1
print(ans)
