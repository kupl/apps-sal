n = int(input())
board = list(map(int,input().split(" ")))
index = list(range(0,n))
ascending = [x for _,x in sorted(zip(board,index))]

winners = n * [""]


for c in reversed(ascending):
	if board[c] == n:
		winners[c] = "B"
	# going down
	toCheck = c - board[c]
	while(toCheck >= 0):
		if winners[toCheck] == "B":
			winners[c] = "A"
		toCheck = toCheck - board[c]
	if winners[c] == "":
		toCheck = c + board[c]
		while(toCheck < n):
			if winners[toCheck] == "B":
				winners[c] = "A"
			toCheck = toCheck + board[c]
	if winners[c] == "":
		winners[c] = "B"
	#print("board at c",board[c])
	#print(c)
	#print(winners)

for i in range(n):
	print(winners[i],end="")
print()
		
	


