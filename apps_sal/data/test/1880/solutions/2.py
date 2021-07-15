n = input()
n = int(n[0] + n[2] + n[4] + n[3] + n[1])
print(str((n ** 5) % 100000).zfill(5))

