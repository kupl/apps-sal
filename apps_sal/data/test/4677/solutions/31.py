n = input()
a = ""
for i in n:
    if i == "0":
        a += i
    elif i == "1":
        a += i
    elif i == "B":
        a = a[:-1]
print(a)
