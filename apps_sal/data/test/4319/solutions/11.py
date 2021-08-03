input()

x = [int(i) for i in input().split()]
a = []

for i in range(len(x)):
    if i == len(x) - 1 or x[i + 1] == 1:
        a.append(x[i])

print(len(a))
print(" ".join([str(x) for x in a]))
