for t in range(int(input())):
    n,k = map(int,input().split())
    if n < k:
        print("NO")
    elif n%2==k%2:
        print("YES")
        print(*([1]*(k-1)+[n-(k-1)]))
    elif n%2==0 and n >= 2*k-1:
        print("YES")
        print(*([2]*(k-1)+[n-2*(k-1)]))
    else:
        print("NO")
