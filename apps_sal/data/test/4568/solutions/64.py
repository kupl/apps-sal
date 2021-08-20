n = int(input())
s = input()
count_list = []
for i in range(1, n):
    x = s[:i]
    y = s[i:]
    xset = set(x)
    xlist = list(xset)
    count = 0
    for j in xlist:
        if j in y:
            count += 1
    count_list.append(count)
print(max(count_list))
