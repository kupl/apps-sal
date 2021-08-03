a, b = input().split()
x = a == "H"
y = b == "H"
if x ^ y:
    print("D")
else:
    print("H")
