s = int(input())
lst = [s]
prev = s
for m in range(2, 1000001):
    if prev % 2 == 0:
        i = int(prev / 2)
    else:
        i = 3 * prev + 1
    if i in lst:
        print(m)
        break
    lst.append(i)
    prev = i
