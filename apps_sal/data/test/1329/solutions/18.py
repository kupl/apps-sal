from itertools import accumulate  # list(accumulate(A))
from collections import defaultdict  # d = defaultdict(int) d[key] += value
import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini] * i for _ in range(j)]

# import bisect #bisect.bisect_left(B, a)
# from collections import Counter # a = Counter(A).most_common()


def factorization(n):
    #arr = []
    #arr = defaultdict(int)
    temp = n
    for i in range(2, int(-(-n**0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            #arr.append([i, cnt])
            arr[i] += cnt

    if temp != 1:
        #arr.append([temp, 1])
        arr[temp] += 1

    if arr == []:
        #arr.append([n, 1])
        arr[n] += 1

    return arr


N = ii()
arr = defaultdict(int)

for i in range(1, N + 1):
    factorization(i)

cnt = [0] * 100

for key, value in arr.items():
    cnt[1] += 1
    cnt[value + 1] += -1

cnt = list(accumulate(cnt))

ans = 0
# print(arr)
# print(cnt)
if cnt[4] > 1:
    #ans += cnt[4] * (cnt[2]-1) * (cnt[2]-2) // 2
    #ans += (cnt[2]-1) * (cnt[2]-2) // 2
    #ans = cnt[2] * (cnt[2]-1) // 2
    #ans += (cnt[2]-2)
    #ans += cnt[4] * (cnt[4]-1) // 2 * (cnt[2]-cnt[4])
    #ans += cnt[4] * (cnt[4]-1) * (cnt[4]-2) // 6
    ans += cnt[4] * (cnt[4] - 1) // 2 * (cnt[2] - 2)

if cnt[24]:
    #ans += (cnt[2]-1)
    #ans += cnt[24] * (cnt[24]-1) // 2 + cnt[24] * (cnt[2] - cnt[24])
    ans += cnt[24] * (cnt[2] - 1)
if cnt[14]:
    #ans += (cnt[4]-1)
    #ans += cnt[14] * (cnt[14]-1) // 2 + cnt[14] * (cnt[4] - cnt[14])
    ans += cnt[14] * (cnt[4] - 1)
if cnt[74]:
    ans += cnt[74]

print(ans)
