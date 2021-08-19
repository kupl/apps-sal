x, y = input().split()
x = int(x)
y = int(y)
a = [input() for i in range(x)]
c = ""
for i in range(y + 2):
    c = c + "#"
print(c)
for i in range(x):
    print("#" + a[i] + "#")
print(c)
