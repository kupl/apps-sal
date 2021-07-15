(n,k) = (int(i) for i in input().split())
order = [int(i) for i in input().split()]
def calculateMinCost(n,k,order):
	cost = 0
	books = set()
	for i in range(n):
		if order[i] in books: continue
		if len(books)!=k:
			cost+=1
			books.add(order[i])
		else:
			lpos = -1
			cc = -1
			for j in books:
				try:
					pos = order[i+1:].index(j)
				except ValueError:
					cc = j
					break
				if pos>lpos:
					lpos = pos
					cc = j
			books.remove(cc)
			books.add(order[i])
			cost += 1
	print(cost)
calculateMinCost(n,k,order)

