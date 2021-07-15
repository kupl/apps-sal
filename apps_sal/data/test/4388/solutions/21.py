a = input()

for i in range(3):
    if a[i] =="1":
        a = a[:i]+"9"+a[i+1:]
    elif a[i] =="9":
        a = a[:i]+"1"+a[i+1:]

print(a)
