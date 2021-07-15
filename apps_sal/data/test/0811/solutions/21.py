a,b=map(int,input().split())
x = a // b
i = 0
s = a
while x >= 1 :
    i = i + x
    s = x + s - x * b
    x = s // b
print(a + i)
