x = input()
lst = []
for i in range(len(x)):
    if x[i:] + x[:i] not in lst:
        lst.append(x[i:] + x[:i])
print(len(lst))
