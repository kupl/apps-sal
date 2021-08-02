from collections import Counter

for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    cnt = Counter()
    bal = 0
    for c in input():
        cnt[bal] += 1
        bal += (c == '0') - (c == '1')
    if bal == 0:
        if cnt[x]:
            print(-1)
        else:
            print(0)
    else:
        ans = 0
        for k in list(cnt.keys()):
            xmk = x - k
            if not xmk % bal and xmk * bal >= 0:
                ans += cnt[k]
        print(ans)
