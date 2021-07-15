import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__

from collections import Counter

def go():
    n = int(input())
    # n,a,b = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter(a)
    m = len(c)
    best=-1
    for cnt in list(c.values()):
        best = max(best,min(cnt,m-1))
        best = max(best,min(cnt-1,m))

    return best

# x,s = map(int,input().split())
t = int(input())
# t = 1
ans = []
for _ in range(t):
    # print(go())
    ans.append(str(go()))
#
print('\n'.join(ans))

