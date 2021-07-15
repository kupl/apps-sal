import math
TC = int(input())
for _ in range(TC):
    n = int(input())
    a = list(map(int, input().split()))
    mark = [False] * n
    prev = 0
    for i in range(n):
        idx = 0
        cur = 0
        for j in range(n):
            if mark[j] == True: continue
            if math.gcd(prev, a[j]) > cur:
                cur = math.gcd(prev, a[j])
                idx = j
        mark[idx] = True 
        prev = cur 
        print(a[idx], end = ' ')
    print()
    

