N = int(input())
lst = []
for i in range(N):
    lst.append(tuple(map(lambda i: int(i), input().split())))
lstP = [xy[0]+xy[1] for xy in lst]
lstM = [xy[0]-xy[1] for xy in lst]
lstP, lstM
z = max(lstP) - min(lstP)
w = max(lstM) - min(lstM)
print(max(z,w))
