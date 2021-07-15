n = input()
y = int(n[0] + n[2] + n[4] + n[3] + n[1])
t =(y ** 5) % 100000
print(str(t).zfill(5))
