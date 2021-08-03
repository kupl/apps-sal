T = int(input())
for t in range(T):
    n, s = map(int, input().split())
    v = list(map(int, input().split()))

    tot = 0
    j = 0
    for i in range(n):
        tot += v[i]
        if tot - max(v[i], v[j]) > s:
            tot -= v[i]
            break
        if v[i] > v[j]:
            j = i

    if tot <= s:
        print(0)
    else:
        print(j + 1)
