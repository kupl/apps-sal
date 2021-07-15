x = int(input())
a = x//11
a *= 2
b = x%11
if b == 0:
    None
elif b <= 6:
    a += 1
else:
    a += 2
print(a)
