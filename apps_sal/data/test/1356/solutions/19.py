def solve():
    s = input()
    
    print (min(len(s), 2 * s.count("a") - 1))
    
def __starting_point():  
    solve()
__starting_point()
