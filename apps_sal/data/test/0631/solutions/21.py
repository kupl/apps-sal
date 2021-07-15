for u in range(int(input())):
    n, m = map(int, input().split())
    x = [int(w) for w in input().split()]
    
    if(sum(x) == m):
        print("YES")
        
    else:
        print("NO")
