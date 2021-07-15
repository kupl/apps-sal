st = input().rstrip()
a = []
for item in st:
    a.append(int(item))

a.reverse()
zero_count = 0
for i, item in enumerate(a):
    if item == 0:
        zero_count += 1
    elif zero_count > 0:
        zero_count -= 1
    else:
        a[i] = 0
a.reverse()
print("".join([str(item) for item in a]))
