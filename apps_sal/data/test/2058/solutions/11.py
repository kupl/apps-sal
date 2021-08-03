a = list(input())
b = list(input())
sum = 0
for i in range(len(a)):
    sum += int(a[i])
    a[i] = sum
a.insert(0, 0)
sum = 0
for i in range(len(b)):
    l = max(0, len(a) - 1 - (len(b) - i))
    r = min(len(a) - 2, i)
    col1 = a[r + 1] - a[l]
    col2 = r - l + 1 - col1
    if b[i] == '0':
        sum += col1
    else:
        sum += col2
print(sum)
