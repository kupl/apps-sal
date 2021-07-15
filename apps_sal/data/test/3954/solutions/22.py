n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

def solve(i, j):
    cur_res = sum(a[i:j+1])
    a1 = sorted(a[i:j+1])
    a2 = sorted(a[:i] + a[j+1:], reverse=True)
    for t in range(min(k, len(a1), len(a2))):
        m = min(a1)
        if a2[t] > m:
            cur_res += a2[t] - m
            a1[a1.index(m)] = a2[t]
    return cur_res

print(max(solve(i, j) for i in range(n) for j in range(i, n)))

