a = input()
b = sorted(a)
print("AC" if a[0] == "A" and "C" in a[2:-1] and b[2] > "Z" else "WA")
