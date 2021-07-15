from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
l = sorted(c.values())
size = len(l)
ans = 0
for i in range(1, l[-1] + 1):
    temp_ans = 0
    cur = i
    pos = size - 1  # pointer of the l array
    while cur <= l[pos] and pos >= 0:  # no index overflow
        temp_ans += cur
        pos -= 1
        if cur & 1:
            break
        cur >>= 1
    ans = max(ans, temp_ans)
print(ans)

