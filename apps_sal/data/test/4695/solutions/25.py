l = ((1,3,5,7,8,10,12),(4,6,9,11),(0,2))
x,y = map(int, input().split())
p = 0
for i in l:
	if x in i and y in i:
		p = 1
		break
ans = 'Yes' if p == 1 else 'No'
print(ans)
