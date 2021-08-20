(n, x) = map(int, input().split())
l = [int(s) for s in input().split()]
pos = 0
count = 1
for i in range(n):
    pos += l[i]
    if pos > x:
        break
    count += 1
print(count)
