def main():
    c_lst = [list(map(int, input().split())) for _ in range(3)]
    c1 = c_lst[0][0] + c_lst[1][1] + c_lst[2][2]
    c2 = c_lst[1][0] + c_lst[2][1] + c_lst[0][2]
    c3 = c_lst[2][0] + c_lst[0][1] + c_lst[1][2]
    
    if c1 == c2 and c2 == c3:
        print('Yes')
    else:
        print('No')
        

def __starting_point():
    main()
__starting_point()
