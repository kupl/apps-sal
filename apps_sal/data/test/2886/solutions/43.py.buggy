arr = input()

chars = dict()

for i in range(len(arr)):
    chars.setdefault(arr[i], [])
    chars[arr[i]].append(i)

for _, inds in list(chars.items()):
    for i in range(len(inds) - 1):
        if inds[i + 1] - inds[i] < 3:
            print((inds[i] + 1, inds[i + 1] + 1))
            return
print((-1, -1))
