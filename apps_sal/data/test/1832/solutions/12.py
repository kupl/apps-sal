import sys
INP = lambda: sys.stdin.readline().strip()
INT = lambda: int(INP())
MAP = lambda: list(map(int, INP().split()))
ARR = lambda: [int(i) for i in INP().split()]
def JOIN(arr, x=''): return x.join([str(i) for i in arr])
def EXIT(x='NO'): print(x); return

for _ in range(INT()):
    n = INT()
    arr = ARR()
    ans = list('ab'*(max(arr)//2 + 1))
    print(JOIN(ans))
    for x in arr:
        ans[x] = 'b' if ans[x]=='a' else 'a'
        print(JOIN(ans))


