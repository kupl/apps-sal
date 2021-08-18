
t = 1
for test in range(1, t + 1):
    n, m, q = list(map(int, input().split()))
    s = input()
    t = input()
    indices = [0 for i in range(n)]
    for i in range(n):
        tmp = s.find(t, i)
        if tmp == -1:
            break
        else:
            indices[tmp] = 1
    pref = [0]
    for i in indices:
        pref.append(i + pref[-1])
    for i in range(q):
        l, r = list(map(int, input().split()))
        if r - l + 1 < m:
            print(0)
            continue
        print(pref[r - m + 1] - pref[l - 1])
