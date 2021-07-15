from operator import itemgetter

N = int(input())
L = []
for n in range(N):
    L.append([int(x) for x in input().split()])
L.sort(key=itemgetter(1))
# print(L)

cnt = 0
while L:
    m = L[0][1]
    L = [l for l in L if l[0] > m]
    cnt += 1
    # print(L)
print(cnt)
        

