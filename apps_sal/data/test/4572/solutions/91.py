s = sorted(list(set(input())))

for i in range(26):
    if chr(ord("a") + i) not in s:
         print(chr(ord("a") + i))
         break
else:
    print("None")
