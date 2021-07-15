def main():
    n = int(input())
    a_lst = list(map(int, input().split()))
    maximum = sum(a_lst) - n
    
    print(maximum)
    

def __starting_point():
    main()
__starting_point()
