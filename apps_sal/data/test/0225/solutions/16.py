arr=[int(x) for x in input().split()]
arr.sort()
if(arr[3]==(arr[0]+arr[1]+arr[2]) or arr[3]+arr[0]==arr[1]+arr[2] or arr[3]+arr[1]==arr[0]+arr[2]):
    print("YES")
else:
    print("NO")

