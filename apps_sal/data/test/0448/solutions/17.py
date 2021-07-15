n, m = map(int, input().split())
kids = list(map(int, input().split()))
kids = [[i+1,x] for i,x in enumerate(kids)]

while len(kids) != 1:
    value = kids[0]
    if m >= value[1]:
        kids.pop(0)
    else:
        value[1] -= m
        kids.pop(0)
        kids.append(value)

print(kids[0][0])
