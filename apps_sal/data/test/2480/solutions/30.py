from collections import defaultdict
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

d = [0]
for i in a:
    a_i = (d[-1] + i) % k
    d.append(a_i)

ans = 0
counter = defaultdict(int)
for i, s in enumerate(d):
    ans += counter[(s-i) % k]
    counter[(s-i) % k] += 1
    if i - k + 1 >= 0:
        counter[(d[i - k + 1]-i+k-1) % k] -= 1

print(ans)


