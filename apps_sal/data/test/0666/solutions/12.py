"""
@author: agavrikov
"""


def sm(x):
    return int(x * (x + 1) / 2)


n = int(input())
st = int(1)
l = int(0)
r = int(1000 * 1000 * 1000)
while l <= r:
    mid = int((l + r) / 2)
    sum = sm(mid)
    if sm(mid) < n:
        st = sum
        l = mid + 1
    else:
        r = mid - 1
print(n - st)
