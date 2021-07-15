k = int(input())

print((50))
l = [i for i in range(50)]

for i in range(50):
    l[i] += k//50
a = k%50
for i in range(a):
    for j in range(50):
        if i == j:
            l[j] += 50
        else:
            l[j] -= 1
print((*l))

