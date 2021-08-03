# cook your dish here
a = int(input())
b = 0
for x in range(1, a + 1):
    c = 0
    for y in range(1, x):
        if x % y == 0:
            c = c + 1
    if c == 1:
        b = b + 1
print(b)
