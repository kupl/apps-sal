s = input()

d = ["z"*5010]*5

k = int(input())
for i in range(len(s)):
    for j in range(i, i+k):
        x = s[i:j+1]
        if x in d or x == '':
            continue
        l = 0
        while l < 5 and x > d[l]:
            l += 1
        # print(k, d[0:k], x, d[k:])
        if l < 5:
            d = d[0:l] + [x] + d[l:]
            d = d[0:5]
        # print(f"->{d}")
# l = list(d)
# l.sort()
# print(l)
# if l[0] == '':
    # l = l[1:]

print((d[k-1]))

