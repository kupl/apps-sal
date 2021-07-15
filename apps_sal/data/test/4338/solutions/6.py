def main():
    arr=input().split()
    n=int(arr[0])
    x=int(arr[1])
    y=int(arr[2])
    if x<=y:
        arr=input().split()
        count=0
        for a in range(n):
            test=int(arr[a])
            if test<=x:
                count+=1
        if count%2==1:
            print(count//2+1)
        else:
            print(count//2)
    else:
        print(n)
main()

