import sys
input = sys.stdin.readline
for nt in range(int(input())):
    (n, k, z) = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[0:k + 1]
    n = len(a)
    pref = [a[0]]
    for i in range(1, n):
        pref.append(pref[-1] + a[i])
    maxx = [a[0]]
    left = [k]
    start = [0]
    for i in range(1, n):
        m = z
        t = k - i
        s = pref[i]
        curr = i
        while m and t:
            if curr == i:
                curr -= 1
                m -= 1
                t -= 1
                s += a[curr]
            else:
                curr += 1
                t -= 1
                s += a[curr]
        maxx.append(s)
        left.append(t)
        start.append(curr)
    ans = 0
    for i in range(n):
        ans = max(ans, maxx[i] + (pref[start[i] + left[i]] - pref[start[i]]))
    print(ans)
