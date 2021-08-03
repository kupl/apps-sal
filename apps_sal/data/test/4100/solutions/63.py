import sys
3
def input(): return sys.stdin.readline().strip()


n, k, q = [int(x) for x in input().split()]
c = [k for i in range(n)]
for _ in range(q):
    c[int(input()) - 1] += 1
for x in c:
    print('Yes' if x > q else 'No')
