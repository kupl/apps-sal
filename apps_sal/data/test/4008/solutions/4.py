def main():
    arr=input().split()
    n=int(arr[0])
    k=int(arr[1])
    arr=input().split()
    store=[[] for x in range(k)]
    colors=[]
    if k>n:
        print("NO")
    elif k==n:
        print("YES")
        string=""
        for x in range(k):
            string+=str(x+1)+" "
        print(string)
        
    else:
        for x in range(k):
            store[x].append(int(arr[x]))
            colors.append(x+1)
        bo_end=False
        for x in range(k,n):
            test=int(arr[x])
            bo=True
            for y in range(k):
                if not test in store[y]:
                    store[y].append(test)
                    colors.append(y+1)
                    bo=False
                    break
            if bo:
                break
            if x==n-1:
                bo_end=True
        if bo_end:
            print("YES")
            string=""
            for x in colors:
                string+=str(x)+" "
            print(string)
        else:
            print("NO")
main()

