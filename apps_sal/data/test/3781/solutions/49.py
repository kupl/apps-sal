from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    if N % 2 == 1:
        print('Second')
    else:
        cnt = defaultdict(int)
        for x in a:
            cnt[x] += 1
        for _, c in list(cnt.items()):
            if c % 2 == 1:
                print('First')
                break
        else:
            print('Second')

