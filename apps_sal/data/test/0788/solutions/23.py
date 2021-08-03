a = list(input())
b = int(0)
for i in range(len(a)):
    if a[i] == "1":
        b += 10
    elif a[i] == "2":
        b += 2
    elif a[i] == "3":
        b += 3
    elif a[i] == "4":
        b += 4
    elif a[i] == "5":
        b += 5
    elif a[i] == "6":
        b += 6
    elif a[i] == "7":
        b += 7
    elif a[i] == "8":
        b += 8
    elif a[i] == "9":
        b += 9
    elif a[i] == "0":
        b += 0
    elif a[i] == "A":
        b += 1
print(int(b))
