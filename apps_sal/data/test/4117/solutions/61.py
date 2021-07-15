def main():
    
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    
    for i in range(N-2):
        
        for j in range(i+1, N-1):
            if a[i] == a[j]:
                continue
            
            for k in range(j+1, N):
                if a[i] == a[k] or a[j] == a[k]:
                    continue
                if a[k] < (a[i] + a[j]):
                    cnt += 1
    
    
    print(cnt)
    
def __starting_point():
    main()
__starting_point()
