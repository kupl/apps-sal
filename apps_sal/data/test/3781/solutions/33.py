t = int(input())
from collections import Counter
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    if n%2:
        print('Second')
    else:
        cnt = Counter(A)
        for val in cnt.values():
            if val%2:
                print('First')
                break
        else:
            print('Second')
