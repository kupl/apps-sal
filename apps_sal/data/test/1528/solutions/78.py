import sys
sys.setrecursionlimit(10**6)

def rec(level, x):
    # print(level,x)
    l_len = pow(2,level+2)-3
    l_len_1 = pow(2,level+1)-3
    num = pow(2,level+1)-1
    num_1 = pow(2,level)-1
    # if level == -2: return
    if level == 0: return 1
    if x == 0: return 0
    if x == 1: return 0
    if x <= l_len_1+1: return rec(level-1,x-1)
    if x <= l_len_1+2: return num_1 + 1
    if x <= l_len-1: return num_1+1 + rec(level-1, x-l_len_1-2)
    else: return num

    # if x == l_len: return num
    # if x <= (l_len-1)//2: return rec(level-1,x-1)
    # if x == (l_len-1)//2+1: return num_1+1
    # else: return num_1+1 + rec(level-1, x-((l_len-1)//2+1))


def main():
    n,x = map(int, input().split())
    print(rec(n,x))

def __starting_point():
    main()
__starting_point()
