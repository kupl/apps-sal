def __starting_point():
    #n, m = list(map(int, input().split()))
    n = int(input())
    t = [0] + list(map(int, input().split()))
    ans = -1
    for i in range(1, n + 1):
        if t[i] - t[i - 1] - 1 >= 15:
            ans = i - 1;
            break;
    if ans != -1:
        print(t[ans] + 15)
    else:
        print(min(90, t[-1] + 15))
    
    
    

__starting_point()
