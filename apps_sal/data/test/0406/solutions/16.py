n = int(input())
ls = list(map(int, input().split()))
ls.sort(reverse=True)

area = 0
pairs = []
i = 0
while i < len(ls)-1:
    if (ls[i] - ls[i+1]) > 1:
        i += 1
    else:
        pairs.append(ls[i+1])
        i += 2
    if len(pairs) == 2:
        area += pairs.pop() * pairs.pop()
print(area)

