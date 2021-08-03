import collections
import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n % 2 == 1:
        print('Second')
    else:
        A = collections.Counter(a)
        count = list(A.values())
        for j in range(len(count)):
            if count[j] % 2 == 1:
                print('First')
                break
        else:
            print('Second')
