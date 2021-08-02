a = input()
a = a.split()
students = int(a[0])
questions = int(a[1])
ans = []
for i in range(students):
    x = input()
    ans.append(x)
weights = input()
weights = weights.split()
for i in range(len(weights)):
    weights[i] = int(weights[i])
n = []
for i in range(questions):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for j in range(students):
        if ans[j][i] == "A":
            a += 1
        if ans[j][i] == "B":
            b += 1
        if ans[j][i] == "C":
            c += 1
        if ans[j][i] == "D":
            d += 1
        if ans[j][i] == "E":
            e += 1
    n.append(max(a, b, c, d, e))
total = 0
for i in range(len(n)):
    total += n[i] * weights[i]
print(total)
