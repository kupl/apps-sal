n = int(input())
a = [int(x) for x in input().split()]
a = sorted(a, reverse=True)
count = 0
prev = None
for x in a:
    if prev != None and prev <= x:
        x = max(prev - 1, 0)
    count += x
    prev = x
print(count)
