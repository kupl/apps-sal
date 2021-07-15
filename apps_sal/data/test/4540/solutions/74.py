N = int(input())
lsA = [0]+list(map(int,input().split()))+[0]
sum1 = 0
for i in range(1,N+2):
    sum1 += abs(lsA[i]-lsA[i-1])
lsans = []
for i in range(1,N+1):
    if lsA[i-1] <= lsA[i] and lsA[i] <= lsA[i+1]:
        lsans.append(sum1)
    elif lsA[i-1] >= lsA[i] and lsA[i] >= lsA[i+1]:
        lsans.append(sum1)
    else:
        div = min(abs(lsA[i-1]-lsA[i]),abs(lsA[i+1]-lsA[i]))
        lsans.append(sum1-2*div)
for i in lsans:
    print(i)
