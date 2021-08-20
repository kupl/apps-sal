from collections import defaultdict
n = int(input())
if n > 26:
    print('-1')
else:
    s = input().strip()
    count = defaultdict(int)
    ans = 0
    for c in s:
        if count[c] >= 1:
            ans += 1
        else:
            count[c] += 1
    print(ans)
