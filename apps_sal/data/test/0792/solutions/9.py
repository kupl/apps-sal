[n, d] = [int(x) for x in input().split(' ')]
A = [int(a) for a in input().split(' ')]

def solve():
    ans = 0
    bal = 0
    minGap = 0
    for i in range(n):
        if A[i] == 0:
            if bal < 0:
                go = min(-bal, minGap)
                minGap -= go
                bal += go
                if bal < 0:
                    ans += 1
                    bal = 0
                    minGap = d
        else:
            bal += A[i]
            if bal > d:
                return -1
            minGap = min(minGap, d - bal)
    return ans

print(solve())
