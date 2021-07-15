def main():
	n = int(input())
	a = [int(x) for x in input().split()]
	b = [int(x) for x in input().split()]
	print(solver(a, b))
	
def solver(a, b):
	a.remove(0)
	b.remove(0)
	index = b.index(a[0])
	if b[index:] + b[:index] == a:
		return "YES"
	else:
		return "NO"

# def isRotation(a, b):
# 	if len(a) != len(b):
# 		return False
# 	else:
# 		b += b
# 		for i in range(len(a)):
# 			if a == b[i: i + len(a)]:
# 				return True
# 		return False

#def rotateLeft(L):
#	L = L[1:] + [L[0]]
#	return L

# L1 = [3, 4, 2, 1]
# L2 = [1, 2, 3, 4]
# print(isRotation(L1, L2))
main()
# a = [1, 0, 2]
# b = [2, 0, 1]
# print(solver(a, b))

# a2 = [1, 0]
# b2 = [0, 1]
# print(solver(a2, b2))

# a3 = [1, 2, 3, 0]
# b3 = [0, 3, 2, 1]
# print(solver(a3, b3))

