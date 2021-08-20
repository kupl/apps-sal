from collections import Counter
for _ in range(int(input())):
    n = int(input())
    lens = []
    cnt = Counter()
    for _ in range(n):
        s = input()
        lens.append(len(s))
        cnt += Counter(s)
    pairs = 0
    singles = 0
    for v in list(cnt.values()):
        (div, mod) = divmod(v, 2)
        pairs += div
        singles += mod
    ans = 0
    lens.sort()
    for len_ in lens:
        (div, mod) = divmod(len_, 2)
        pairs -= div
        if mod:
            if singles:
                singles -= 1
            else:
                singles = 1
                pairs -= 1
        if pairs < 0:
            break
        ans += 1
    print(ans)
