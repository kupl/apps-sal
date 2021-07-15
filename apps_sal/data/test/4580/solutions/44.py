n = input()
a = list(map(int,input().split()))

s = set()
b = 0
for i in a:
    if i < 3200:
        s.add(i//400)
    else:
        b += 1
else:
    min = len(s)
    print(max(min, 1), min + b)
