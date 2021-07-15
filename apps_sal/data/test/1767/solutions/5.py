read = lambda: list(map(int, input().split()))
n = int(input())
a = list(read())
b = list(read())
f1 = 0
for i in a:
    f1 |= i
f2 = 0
for i in b:
    f2 |= i
print(f1 + f2)

