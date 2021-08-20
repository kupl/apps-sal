(a, b) = list(map(int, input().split()))
a = list(map(str, input().split()))
c = 0
for i in a:
    if i.count('4') + i.count('7') <= b:
        c += 1
print(c)
