def main():
    X, Y = list(map(int, input().split()))
    ans = 1
    cnt = X
    for _ in range(300):
        cnt *= 2
        if cnt <= Y:
            ans += 1
        else:
            print(ans)
            return
        
def __starting_point():
    main()

__starting_point()
