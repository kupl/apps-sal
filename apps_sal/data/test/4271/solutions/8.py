N = int(input())
lsA = list(map(int,input().split()))
lsB = [0]+list(map(int,input().split()))
lsC = [0]+list(map(int,input().split()))
sumB = sum(lsB)
for i in range(N-1):
    if lsA[i]+1 == lsA[i+1]:
        sumB += lsC[lsA[i]]
print(sumB)
