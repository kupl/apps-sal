def binarysearch(A, key):
    l = -1
    r = len(A)
    while r > l+1:
        m = (l + r) // 2
        if A[m] > key:
            r = m
        else:
            l = m
    return l

n = int(input())
lst = [int(i) for i in input().split()]
lst.sort()
m = int(input())
t = []
for i in range(m):
	x = int(input())
	t.append(binarysearch(lst, x))
for i in t:
	print(i+1)


