def __starting_point():

    x = int(input())
    
    ans = (x // 500)
    if ans > 0:
        x = x - (500 * ans)
        ans *= 1000
    
    ans += (x // 5) * 5
    print(ans)
__starting_point()
