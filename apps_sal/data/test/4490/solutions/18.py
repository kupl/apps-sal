n = input()
c = ["A", "T", "G", "C"]
a = ["T", "A", "C", "G"]
for i in range(4):
    if n == c[i]:
        print(a[i])
        break
