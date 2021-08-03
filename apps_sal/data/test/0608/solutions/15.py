n = int(input())
a = input()
b = a.split()
ch = 0
k = 0

for i in range(len(b)):
    if b[i] == "4" or b[i] == "5":
        ch += 1
        if ch == 3:
            k += 1
            ch = 0
    else:
        ch = 0

print(k)
