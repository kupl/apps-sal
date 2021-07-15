l = [2, 1] + [0] * 100
for i in range(2, 87):
    l[i] = l[i - 1] + l[i - 2]
print(l[int(input())])
