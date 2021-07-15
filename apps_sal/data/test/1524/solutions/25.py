a = input()
b = int(len(a))
c = []

for i in range(b):
    c.append(int(0))

d = str()

if a[b-1] == "L":
    d = "R"
else:
    d = "L"

a = a+d

temp = int(1)

for i in range(b):
    if a[i] == a[i+1]:
        c[i] += 0
        temp += 1
    elif a[i] != a[i+1] and a[i] == "R":
        c[i+1] += temp // 2
        c[i] += (temp - temp // 2)
        temp = 1
    else:
        c[i-temp] += temp // 2
        c[i-temp+1] += (temp - temp // 2)
        temp = 1
f = [str(s) for s in c]
e = " ".join(f)
print(e)
