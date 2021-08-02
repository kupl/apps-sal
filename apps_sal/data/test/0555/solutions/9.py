n = input()
n1 = ""
if int(n[0]) != 9:
    n1 += str(min(int(n[0]), 9 - int(n[0])))
else:
    n1 += "9"
for i in n[1:]:
    n1 += str(min(int(i), 9 - int(i)))
print(n1)
