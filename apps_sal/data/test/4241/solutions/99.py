s = list(input())
t = list(input())

min = len(t)

for i in range(0,len(s) - len(t)  + 1):
    count = 0
    for j in range(0,len(t)):
        if s[i + j] != t[j]:
            count += 1

    if count < min:
        min = count
print(min)
