
def helper(x):
    res = 0
    while x > 0:
        if x % 2 == 0:
            x //= 2
        else:
            res += 1
            x //= 2
    return res


n = int(input())
a = list(map(int, input().split()))
d = dict()

for element in a:
    res = helper(element)
    if d.__contains__(res):
        d[res] += 1
    else:
        d[res] = 1

ans = 0
for element in d:
    ans += d[element] * (d[element] - 1) / 2

print(int(ans))
