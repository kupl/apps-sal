def abc128c_switches():
    import itertools
    n, m = map(int, input().split())
    s = []
    for _ in range(m):
        v = list(map(int, input().split()))
        v = v[1:]
        s.append(v)
    p = list(map(int, input().split()))
    pattern = itertools.product([0,1], repeat=n)
    result = 0
    for pat in pattern:
        cnt = 0
        for i in range(m):
            total = 0
            for j in s[i]:
                if pat[j-1] == 1:
                    total += 1
            if total %2==p[i]:
                cnt +=1
        if cnt == m:
            result += 1
    print(result)

abc128c_switches()
