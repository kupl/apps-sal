import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))
from collections import deque

def main():
    K = int(input())
    # cnt = 0
    # dq = deque(['1','2','3','4','5','6','7','8','9'])
    # while cnt < K:
    #     cnt += 1
    #     d = dq.popleft()
    #     a = int(d[-1])
    #     if a == 0:
    #         dq.append(d+str(0))
    #         dq.append(d+str(1))
    #     elif a == 9:
    #         dq.append(d+str(8))
    #         dq.append(d+str(9))
    #     else:
    #         for i in range(a-1, a+2):
    #             dq.append(d+str(i))
    # print(d)

    runrun_lst = []
    def rec(num_of_digit, runrun_val):
        runrun_lst.append(runrun_val)
        if num_of_digit == 10: return
        for i in range(-1, 2):
            add = (runrun_val%10) + i
            if 0 <= add <= 9: rec(num_of_digit+1, runrun_val*10+add)

    for v in range(1, 10):
        rec(1, v)
    runrun_lst.sort()
    print(runrun_lst[K-1])

def __starting_point():
    main()
__starting_point()
