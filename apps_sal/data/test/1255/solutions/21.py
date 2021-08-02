n = int(input())
max = 1

a, b = input().split(" ")
counter = 1
for i in range(n - 1):
    c, d = input().split(" ")
    if (a == c and b == d):
        counter += 1
        if counter > max:
            max = counter
    else:
        a = c
        b = d
        counter = 1

print(max)
