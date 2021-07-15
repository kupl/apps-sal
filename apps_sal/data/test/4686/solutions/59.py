a = list(input())
a.sort()
b = list(set(a))
for i in range(len(b)):
    if a.count(b[i]) % 2 == 0:
        continue
    else:
        print("No")
        return
print("Yes")
