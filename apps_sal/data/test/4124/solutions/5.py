a = input().strip()
b = input().strip()
common = 0
while True:
    if common >= min(len(a), len(b)):
        break
    if a[-(common + 1)] != b[-(common + 1)]:
        break
    common += 1
print(len(a) - common + len(b) - common)
