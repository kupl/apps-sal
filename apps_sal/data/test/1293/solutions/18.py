n = int(input())
b = input().split()
counter = 0
x = 0
for i in b:
    counter += abs(x - int(i))
    x = int(i)
print(counter)
