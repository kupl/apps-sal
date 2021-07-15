from collections import Counter

n = int(input())
c = Counter(list(map(int, input().split())))

ans = 0
for k, v in list(c.items()):
    if k == 0:
        if n%2==0 and v > 2:
            print((0))
            return
        elif n%2==1 and v > 1:
            print((0))
            return
    else:
        ans += 1
        if v > 2:
            print((0))
            return

print((pow(2, ans, 10**9+7)))

