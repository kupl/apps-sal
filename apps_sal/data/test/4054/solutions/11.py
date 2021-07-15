a=input().split()
ing=[1,1,2,7,4]
b=[int(i) for i in a]
c=[int(b[i]/ing[i]) for i in range(len(a))]
print(min(c))
