mini, maxi = 1, 0
indexes = {}
ans = []
for q in range(int(input())):
	cmd = input().split()
	idx = int(cmd[1])
	if cmd[0]=="L":
		mini-=1
		indexes[idx]=mini
	elif cmd[0]=="R":
		maxi+=1
		indexes[idx]=maxi
	else:
		ind = indexes[idx]
		ans.append(min(ind-mini,maxi-ind))
print(*ans,sep="\n")

