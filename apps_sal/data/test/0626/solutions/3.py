import sys


#sys.stdin = open("input.txt")
#sys.stdout = open("output.txt", "w")

n = int(input())
lst = [int(i) for i in input().split()]
was = [False for i in range(n)]
cur = 0
ind = 0
ans = 0
curdir = 1
while cur < n:
    #print("ind = ", ind)
    if not was[ind]:
        if lst[ind] <= cur:
            cur += 1
            was[ind] = True
            if cur == n:
                break
    if ind == n - 1 and curdir > 0 or ind == 0 and curdir < 0:
        curdir = -curdir
        ans += 1
    ind += curdir

print(ans)
