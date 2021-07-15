n = input()
a = 0
for i in n:
  a += int(i)
print("Yes" if int(n) % a == 0 else "No")
