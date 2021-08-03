a = input()
b = input()
print("YNEOS"[len(a) != len(b) or "1" in set(a) ^ set(b)::2])
