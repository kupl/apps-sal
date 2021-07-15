
import sys
def __starting_point():
    n, q = list(map(int, sys.stdin.readline().split()))
    arr = sys.stdin.readline()
    total = [0]*n
    if arr[0] == '1':
        total[0] = 1
    else:
        total[0] = 0
    for i in range(1, n):
        if arr[i] == '1':
            total[i] = total[i-1]+1
        else:
            total[i] = total[i-1]
    mod = 10**9+7
    for i in range(q):
        l, r = list(map(int, sys.stdin.readline().split()))
        l -= 1
        r -= 1
        length = r-l+1
        ans = pow(2, length, mod)
        ans = (ans-1+mod) % mod
        if l == 0:
            zeroes = length-total[r]
        else:
            zeroes = length-(total[r]-total[l-1])
        sub = pow(2, zeroes, mod)
        sub = (sub-1+mod) % mod
        ans = (ans-sub+mod) % mod
        print(ans)

__starting_point()
