import math 
def main():
    n, k = list(map(int, input().split()))
    P = list(map(int, input().split()))
    P.sort()

    M = k
    count = 0
    for num in P:
        f = math.ceil(math.log2(num/M)) - 1
        # print(num/M, f)
        if f < 1:
            pass
        else:
            count += f
        M = max(M, num)
    print(count)

def __starting_point():
    # nonlocal stime
    # stime = time.clock()
    main()

__starting_point()
