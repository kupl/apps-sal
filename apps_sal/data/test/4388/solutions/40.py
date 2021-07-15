a = list(input())

for i in range (0, len(a)):
    if a[i] == "1":
        a[i] = "9"
    elif a[i] == "9":
        a[i] = "1"
    print(a[i], end = "")
