n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
q={1}
for i in range(n-1, -1, -1):
    if arr[i] not in q:
        q|={arr[i]}
        print(arr[i])

