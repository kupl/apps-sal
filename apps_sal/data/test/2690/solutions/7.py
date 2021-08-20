a = input()
a1 = 'abc'
lower = []
upper = []
for i in range(len(a1)):
    for j in range(len(a)):
        if a1[i] == a[j]:
            lower.append(j)
            break
for i in range(len(a1)):
    for j in range(len(a)):
        if a1[i] == a[j]:
            t = j
    upper.append(t)
ans = 1
for i in range(len(lower)):
    for j in range(len(lower)):
        if i != j:
            ans = max(abs(upper[j] - lower[i]), ans)
print(ans)
