def main():
    
    n,m = list(map(int,input().split()))
    l = list(input())[::-1]
    ans = []
    i = 0
    l[0] = 0

    while i < n+1:
        if l[i] == 0:
            a = -1
            for j in range(m,0,-1):
                if i+j < n+1 and l[i+j] != "1":
                    a = i+j
                    ans.append(j)
                    l[a] = 0
                    break
            if a == -1:
                print((-1))
                return
            else:
                i = a
            
            if l[-1] == 0:
                break
    
    print((*ans[::-1]))

def __starting_point():
    main()

__starting_point()
