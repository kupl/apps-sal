N = int(input())
Red = [[int(T) for T in input().split()] for TN in range(0,N)]
Red.sort(key=lambda X:X[1],reverse=True)
Blue = [[int(T) for T in input().split()] for TN in range(0,N)]
Blue.sort(key=lambda X:X[0])
Count = 0

for TB in range(0,N):
    DelInd = -1
    for TR in range(0,len(Red)):
        if Blue[TB][0]>Red[TR][0] and Blue[TB][1]>Red[TR][1]:
            DelInd = TR
            break
    if DelInd!=-1:
        del Red[DelInd]
        Count += 1
print(Count)
