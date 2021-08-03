import bisect
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a = sorted(a)
b = sorted(b)
c = sorted(c)
b_ans = [0] * len(b)
for i in range(len(b)):
    b_ans[i] = bisect.bisect_left(a, b[i])

ruiseki_b = [0]
for i in range(len(b_ans)):
    ruiseki_b.append(ruiseki_b[i] + b_ans[i])
ans = 0
for i in range(len(c)):
    ans += ruiseki_b[bisect.bisect_left(b, c[i])]
print(ans)
