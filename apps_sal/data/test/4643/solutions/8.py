import time
t = time.time() + 1.9
a = [int(i) for i in input().split(' ') if i]
a = a[1:a[1] + 1]
a.sort()
while time.time() < t:
    pass
for i in a:
    print(i, end=' ')
print()
