n = input()
arr = []
for i in range(10):
    s = ""
    for j in range(3):
        s += str(i)
    arr.append(s)

if n[0:3] in arr or n[1:4] in arr:
    print("Yes")
else:
    print("No")
