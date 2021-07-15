def solve():
    S = input()
    T = input()
    n = len(S)
    m = len(T)
    if(n >= 1 and n <= 10 and m-n == 1):
        if(T[:m-1] == S):
            print("Yes")
            return
    print("No")



def __starting_point():
    solve()
    


__starting_point()
