from functools import reduce

n, k = map(int, input().split())

flip = 2 * k + 1

l = -(-n // flip)

max = (k + 1) + (l - 1) * flip
i = k + 1
if max > n:
    i -= (max - n)

arr = []
# if n%flip > k:
# i = k+1
while i <= n:
    arr.append(i)
    i += flip
# else:
    # i = 1
    # while i <= n:
    # arr.append(i)
    # i += flip

s = reduce(lambda x, y: str(x) + ' ' + str(y), arr)
print(l)
print(s)
