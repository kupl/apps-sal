import operator
n = int(input()) 
arr=[]
for i in range(n):
    arr.append([int(element) for element in input().split()])
arr = sorted(arr, key=operator.itemgetter(1,0,2), reverse= True) 
heigh = [0 for i in range(n)] 
seq = [] 
for i in range(n):
    while len(seq) > 0 and arr[seq[-1]][0] >= arr[i][1] :
        seq.pop()
    if len(seq) > 0 :
        heigh[i] = heigh[seq[-1]] 
    heigh[i] += arr[i][2] 
    seq.append(i)
print(max(heigh))

