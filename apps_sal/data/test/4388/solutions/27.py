a = input()
l1 = []
l2 = []
for i in range(len(a)):
    l1.append(a[i:i + 1])
for i in range(len(a)):
    l2.append(str(abs(int(l1[i]) - 10)))
print("".join(l2))
