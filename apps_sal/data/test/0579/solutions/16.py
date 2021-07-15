import sys
input = sys.stdin.readline



def main():
    n, k = list(map(int, input().split()))
    p = [int(x)-1 for x in input().split()]
    c = list(map(int, input().split()))
    
    doubling = [[0]*n for i in range(31)]
    doubling_max = [[0]*n for i in range(31)]
    place = [[0]*n for i in range(31)]
    
    ans = -1000000000
    for i in range(n):
        sub = c[p[i]]
        if sub >= 0:
            break
        if ans < sub:
            ans = sub
        if i == n-1:
            print(ans)
            return
            
    
    for i in range(31):
        if i == 0:
            for j in range(n):
                doubling[i][j] = c[p[j]]
                place[i][j] = p[j]
            continue
        for j in range(n):
            place[i][j] = place[i-1][place[i-1][j]]
            doubling[i][j] = doubling[i-1][j]+doubling[i-1][place[i-1][j]]
    
    for i in range(31):
        if i == 0:
            for j in range(n):
                doubling_max[i][j] = doubling[i][j]
            continue
        for j in range(n):
            doubling_max[i][j] = max(doubling_max[i-1][j], doubling[i-1][j]+doubling_max[i-1][place[i-1][j]])
    
    ans = 0
    judge = []
    key = 0
    while k:
        if k%2:
            judge.append(key)
        k //= 2
        key += 1
    judge.reverse()
    
    for i in range(n):
        pl = i
        key = 0
        for j in range(len(judge)):
            if ans < key+doubling_max[judge[j]][pl]:
                ans = key+doubling_max[judge[j]][pl]
            key += doubling[judge[j]][pl]
            pl = place[judge[j]][pl]
        

    print(ans)
        
    


    
    
def __starting_point():
    main()

__starting_point()
