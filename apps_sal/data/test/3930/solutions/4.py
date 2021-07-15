import math

n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
if abs(k) > 1:
    valid = [k ** i for i in range(0, math.ceil(math.log(n * 1e9) / math.log(abs(k))) + 1)]
elif k == -1:
    valid = [1, -1]
else:
    valid = [k]
# print(math.log(n * 1e9) / math.log(abs(k)))
# print(valid)

s = 0
ans = 0
count = {s : 1}
for i in a:
    s += i
    for j in valid:
        if count.get(s - j):
            ans += count[s - j]
    if count.get(s):
        count[s] += 1
    else:
        count[s] = 1
print(ans)

