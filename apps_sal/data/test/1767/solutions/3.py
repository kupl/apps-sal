n = int(input())
f1 = f2 = 0
for x in input().split():
    f1 |= int(x)
for x in input().split():
    f2 |= int(x)
print(f1 + f2)
