n = int(input())

huh = list(map(int, input().split()))
a = {}
for i in huh:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
        
maxx = 0

for i in a:
    if a[i] > maxx:
        maxx = a[i]
print(maxx)
