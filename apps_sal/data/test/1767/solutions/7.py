n = int(input())
a = 0
for i in input().split():
    a |= int(i)
b = 0
for i in input().split():
    b |= int(i)
print(a + b)
