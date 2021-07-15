N,H = map(int,input().split())
ls = []
for i in range(N):
    a,b = map(int,input().split())
    ls.append([a,b])
ls.sort()
ls.sort(key=lambda x:-x[0])
mainkatana = ls.pop(0)
ls.sort(key=lambda x:-x[1])
ls.append([0,0])
ii = 0
while ls[0][1] >= mainkatana[0] and H > mainkatana[1]:
    ii += 1
    nage = ls.pop(0)
    H -= nage[1]
cut = max(0,-(-(H-mainkatana[1])//mainkatana[0]))
ii += cut
if H > 0:
    ii += 1
print(ii)
