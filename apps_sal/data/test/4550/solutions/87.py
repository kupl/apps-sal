a, b, c = map(int, input().split())

li = sorted([a, b, c])
ans = 'No'
if sum(li[:2])==li[2]:
    ans ='Yes'
print(ans)
