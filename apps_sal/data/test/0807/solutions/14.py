import sys, math, heapq, random, collections, bisect

def main():
    # sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')

    n = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    c_lst = lst[:]
    c_lst.sort()

    if c_lst == lst:
        print(0)

    else:
        c_lst.reverse()
        mx = 0
        rp = 0

        for i in c_lst:
            if rp == i:
                if lst[idx_+1:].index(i) < len(lst[idx_+1:])-1:
                    idx = lst[idx_+1:].index(i)
    
                    if lst[idx_+1:][idx]-lst[idx_+1:][idx+1] > mx:
                        mx = lst[idx_+1:][idx]-lst[idx_+1:][idx+1]
                        
                idx_ = idx+idx_+1

            elif lst.index(i) < len(lst)-1:
                idx = lst.index(i)
                idx_ = idx
                rp = i

                if lst[idx]-lst[idx+1] > mx:
                    mx = lst[idx]-lst[idx+1]

            elif i < mx:
                break

        if (mx-n[1]) > 0:
            print(mx-n[1])
            
        else:
            print(0)

    # sys.stdin.close()
    # sys.stdout.close()

def __starting_point():
    main()

__starting_point()
