c = int(input())
x = 0
for i in range(c):
    s = input()
    if(s.count('++')):
        x = x + 1
    else:
        x = x - 1
print(x)
