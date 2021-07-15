w = input()
x = set(w)
y = []
for i in x:
    y.append(w.count(i))
for j in y:
    if j%2 == 0:
        continue
    else:
        print("No")
        return
print("Yes")

