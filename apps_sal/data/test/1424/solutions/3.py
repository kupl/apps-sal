n,m,k = [int(x) for x in input().split()]
arr = [int(input()) for i in range(m+1)]

def calc(x):
	return bin(x^arr[-1]).count('1')<=k
print(sum(map(calc,arr[:-1])))
