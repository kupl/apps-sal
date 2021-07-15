x = int(input())
a = x
x += 1
if len(str(x))-str(x).count('0') <= 1:
    b = x;
else:
    b = int(str(int(str(x)[0])+1)+'0'*(len(str(x))-1))
print(b-a)
