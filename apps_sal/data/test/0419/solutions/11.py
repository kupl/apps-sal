from sys import stdin

a = int(stdin.readline(), 2)
b = 1
count = 0
while b < a:
    b *= 4
    count += 1
print(count)
