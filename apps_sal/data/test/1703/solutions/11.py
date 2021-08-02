n = int(input())
d = dict()
for i in range(n):
    k = input()
    right = 0
    left = 0
    for i in k:
        if i == '(':
            right += 1
        else:
            if right == 0:
                left += 1
            else:
                right -= 1
    if left == 0 or right == 0:
        c = left - right
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
s = list(d.keys())
s.sort()
k = 0
for i in s:
    if i > 0:
        break
    if -i in d:
        k += d[i] * d[-i]
print(k)
