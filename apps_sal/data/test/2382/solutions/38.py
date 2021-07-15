from heapq import heapify, heappush, heappop

def solve():
    N = int(input())
    Ss = list(map(int, input().split()))

    Ss.sort(reverse=True)
    pow2s = [2**i for i in range(N)]

    PQs = [[-Ss[0]] for _ in range(N)]
    nums = [0] * N
    tm0 = 0
    for S in Ss[1:]:
        for tm in range(tm0, N):
            if nums[tm] >= pow2s[tm]:
                tm0 = tm
            else:
                if -PQs[tm][0] > S:
                    heappop(PQs[tm])
                    nums[tm] += 1
                    for i in range(tm+1, N):
                        heappush(PQs[i], -S)
                    break
        else:
            return False

    return True

if solve():
    print('Yes')
else:
    print('No')

