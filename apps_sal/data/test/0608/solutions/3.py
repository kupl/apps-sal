n = int(input())
a = []
r = 0
a = input().split()
for i in range(n):
    a[i] = int(a[i])
scane = 0
while scane < (n - 2):
    plus = 0
    if a[scane] > 3:
        plus += 1
        if a[scane + 1] > 3:
            plus += 1
            if a[scane + 2] > 3:
                r += 1
                plus += 1
        scane += (plus)
    else:
        scane += 1
print(r)
