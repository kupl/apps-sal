def C(n, r):
    ret = 1
    for i in range(r):
        ret = ret * (n - i) // (i + 1);
    return ret

def f(N):
    N = [int(ch) for ch in reversed(str(N))]
    cnt, nonzero = 0, 0
    for k in range(len(N)-1, -1, -1):
        if N[k] > 0:
            for i in range(4 - nonzero):
                cnt += C(k, i) * pow(9, i)
            nonzero += 1
            for i in range(4 - nonzero):
                cnt += (N[k] - 1) * C(k, i) * pow(9, i)
        if nonzero > 3:
            break
    return cnt

for run in range(int(input())):
    l, r = list(map(int, input().split()))
    print(f(r+1) - f(l))

