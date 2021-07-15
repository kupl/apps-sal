import sys
import bisect
input = sys.stdin.readline

def main():
    n, q = list(map(int, input().split()))

    ans = 0
    min1, min2 = n-2, n-2
    judge1 = [-n-1]
    judge2 = [-n-1]
    dict1 = dict()
    dict2 = dict()
    dict1[-n-1] = n-2
    dict2[-n-1] = n-2

    for i in range(q):
        query, x = list(map(int, input().split()))

        if query == 1:
            index = bisect.bisect(judge1, -x)-1
            key = dict1[judge1[index]]
            ans += key
            if min1 > x-2:
                min1 = x-2
                judge1.append(-x)
                dict1[-x] = key
                dict2[judge2[-1]] = min1
        else:
            index = bisect.bisect(judge2, -x)-1
            key = dict2[judge2[index]]
            ans += key
            if min2 > x-2:
                min2 = x-2
                judge2.append(-x)
                dict2[-x] = key
                dict1[judge1[-1]] = min2

    print(((n-2)**2 - ans))
    
    
    
    
def __starting_point():
    main()

__starting_point()
