first = input()
second = input()
x = input()
y = ''
first += first.upper()
second += second.upper()
for i in range(len(x)):
    if x[i] in first:
        y += second[first.index(x[i])]
    else:
        y += x[i]
print(y)
