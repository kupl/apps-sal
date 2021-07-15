n = int(input())
arr = dict()
l = 0
st = 0
for i in input().split():
    i = int(i)
    if(i in arr):
        arr[i].append(l)
    else:
        arr[i] = [l]
    if(l == 0): st = i
    l+=1
    '''
for i in arr:
    arr[i].sort()
    '''



sets = 1
keys = list(arr.keys())

ma = arr[st][-1]
l = len(keys)
for j in range(l-1):
    i = keys[j]
    k = keys[j+1]
    if(ma<arr[k][0]):
        sets+=1
        ma = arr[k][-1]
        #print(ma,k)
        
    elif(ma<arr[k][-1]):
        ma = arr[k][-1]
#print(sets)
print(pow(2,sets-1,998244353))
