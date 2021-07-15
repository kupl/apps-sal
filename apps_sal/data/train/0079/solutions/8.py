from sys import stdin, stdout
import math
import bisect

def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

def solve(n):
    dv = [n]
    x = 2
    while x*x <= n:
        if n%x == 0:
            dv.append(x)
            if x != n//x:
                dv.append(n//x)
        x += 1
    dv = sorted(dv)
    ans = [0]*len(dv) 

    ans[0], ans[-1] = dv[0], dv[-1]
    seen = {dv[0], dv[-1]}
    cur_prime = dv[0]
    min_prime = dv[0]
    while len(seen) < len(dv):
        for x in dv:
            if x in seen: continue
            if min_prime == -1:
                min_prime = x

            if cur_prime == -1:
                if ans[len(seen)-2]%x == 0:
                    cur_prime = x
                    ans[len(seen)-1] = x
                    seen.add(x)
            else:
                if x%cur_prime == 0:
                    ans[len(seen)-1] = x
                    seen.add(x)
        if cur_prime == -1:
            cur_prime = min_prime
        else:
            cur_prime = -1
        min_prime = -1
    cnt = 0
    for i in range(1, len(ans)):
        if gcd(ans[i], ans[i-1]) == 1:
            cnt += 1
    print(" ".join(map(str, ans)))
    print(cnt)

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    solve(n)

#for i in range(2, 50):
#    solve(i)

