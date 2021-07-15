n = int(input())
n = str(n)
# nの二桁目と三桁目が同じで、それが一桁目か四桁目がと同じならYes
if n[1] == n[2]:
    if n[0] == n[1] or n[2] == n[3]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
