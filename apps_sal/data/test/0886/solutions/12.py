N = input()

arr = []
for i in range( 0 , len(N)-1):
    if int(N[i])%2 == 0:
        arr.append( {"index":i , "num":N[i]} )
#print(arr)

if len(arr) == 0:
    print("-1")
else:
    lastIndex = len(N) - 1  
    lastNum = N[len(N)-1]
    resIndex = -1
    resNum = -1
    for numDict in arr:
        if int(numDict["num"]) < int(lastNum):
            resIndex = numDict["index"]
            resNum = numDict["num"]
            break
    if resIndex == -1:
        resIndex = arr[len(arr)-1]["index"]
        resNum = arr[len(arr)-1]["num"]

    print( N[0:resIndex] + lastNum + N[resIndex+1:lastIndex] + resNum )
    

