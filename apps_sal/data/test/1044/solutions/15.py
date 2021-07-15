n=int(input())
l=list(input().split())
l=[int(i) for i in l]
winner=1
for i in l:
	if not i%2:
		winner=not winner
		print(int(winner)+1)
	else:
		print(int(winner)+1)


