import array


def helper(x):
    ret = 0
    while x > 0:
        if x % 2 == 0:
            x //= 2
        else:
            ret += 1
            x //= 2
    return ret


n = int(input())
a = list(map(int, input().split()))
d = [0] * 10000

for element in a:
    res = helper(element)
    d[res] += 1

ans = 0
for element in d:
    ans += element * (element - 1) / 2

print(int(ans))
