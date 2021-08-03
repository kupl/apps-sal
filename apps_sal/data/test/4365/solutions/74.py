k = int(input())
print(int((k / 2)**2 if k % 2 == 0 else (k // 2) * ((k // 2) + 1)))
