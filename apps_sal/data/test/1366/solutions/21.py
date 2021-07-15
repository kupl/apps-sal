"""
	Author		: Arif Ahmad
	Date  		: 
	Algo  		: 
	Difficulty	: 
"""

def main():
	n = int(input())
	
	a = [None] * n
	b = [None] * n
	for i in range(n):
		a[i], b[i] = list(map(int, input().split()))
		
	for i in range(n):
		for j in range(n):
			if i == j: continue
			if a[j] == b[i]: a[j] = -1

	ans = 0
	for item in a:
		if item != -1: ans += 1
	
	print(ans)


def __starting_point():
    main()
    

__starting_point()
