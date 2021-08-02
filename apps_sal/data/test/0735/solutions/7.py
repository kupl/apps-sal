n = input()
thelist = input()
final = []
now = thelist.split()
for item in now:
    final.append(int(item))
begin = sorted(final)
indices = []
i = 0
length = len(final)
while i < length:
    if final[i] != begin[i]:
        indices.append(i)
    i += 1
all = len(indices)
if len(indices) != 0:
    x = indices[0]
    y = indices[all - 1]
    switched = []
    p = 0
    while p < x:
        switched.append(final[p])
        p += 1
    j = 0
    while j <= (y - x):
        switched.append(final[y - j])
        j += 1
    q = y + 1
    while q < length:
        switched.append(final[q])
        q += 1
    switchable = "yes"
    z = 0
    while z < len(begin):
        if switched[z] != begin[z]:
            switchable = "no"
            break
        z += 1
    if switchable == "yes":
        print("yes")
        print(x + 1, y + 1)
    else:
        print("no")

else:
    print("yes")
    print("1 1")
