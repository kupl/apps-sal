n = int(input())
max = 1
a = input()
counter = 1
for i in range(n - 1):
    c = input()
    if a == c:
        counter += 1
        if counter > max:
            max = counter
    else:
        a = c
        counter = 1
print(max)
