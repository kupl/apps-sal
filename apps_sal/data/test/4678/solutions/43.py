def main():
    N = int(input())
    a = list(map(int, input().split()))
    
    DP = [0] * N
    max_i = 0
    
    for i in range(1, N):
        if a[max_i] > a[i]:
            DP[i] += (a[max_i]-a[i])
        elif a[max_i] < a[i]:
            max_i = i
            
    
    print(sum(DP))

def __starting_point():
    main()
__starting_point()
