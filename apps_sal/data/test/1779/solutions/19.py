a = list(input().strip())
b = list(input().strip())
x = list(input().strip())
m = []
for i in x:
    if i.isupper():
        i = i.lower()
        for j, k in zip(a, b):
            if j == i:
                m.append(k.upper())
    elif i.islower():
        for j, k in zip(a, b):
            if j == i:
                m.append(k)
    elif i.isdigit():
        m.append(i)
for i in m:
    print(i, end="")
