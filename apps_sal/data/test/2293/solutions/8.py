m, n = map(int, input().split())
l = []
# print(m,n)
for i in range(m):
    l += [list(map(int, input().split()))]
l = [set(i[1:]) for i in l]
# k=0
# print(n,m)
for i in range(m):
    for j in range(i + 1, m):
        # print(a,b,a.intersection(b))
        if len(l[i].intersection(l[j])) == 0:
            print('impossible')
            return
    """count=0
				for j in range(m):
					if i in l[j]:
						count+=1
				if count==m:
					print('possible')
					return"""
print('possible')
