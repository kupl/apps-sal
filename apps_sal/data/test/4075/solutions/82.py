n, m = map(int, input().split())
k = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))
 
ans = 0
for i in range(2**n):
    light = 0
    for ki, j in enumerate(k):
        switch = 0
        for s in j[1:]:
            if i & (1 << s-1):
                switch += 1
        if switch % 2 == p[ki]:
            light += 1
    if light == m:
        ans += 1
print(ans)
