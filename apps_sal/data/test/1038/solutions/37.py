A, B = map(int, input().split())
if A % 2:
    s1 = ((A + 1) // 2) % 2
else:
    s1 = ((A // 2) % 2) ^ A
if B % 2:
    s2 = ((B + 1) // 2) % 2
else:
    s2 = ((B // 2) % 2) ^ B
print(s1 ^ s2 ^ A)
