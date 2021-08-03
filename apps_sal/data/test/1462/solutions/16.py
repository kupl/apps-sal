this = input()
hurry = this.split()
n = int(hurry[0])
k = int(hurry[1])
then = input()
thelist = []
i = 0
while i < len(then):
    thelist.append(then[i])
    i += 1
# print(thelist)

checked = []
counts = []
for item in thelist:
    if item not in checked:
        checked.append(item)
        counts.append(thelist.count(item))
# print(checked)
# print(counts)
thetotal = 0
while k > 0:
    x = max(counts)
    if x >= k:
        print(thetotal + k * k)
        k = 0
    else:
        thetotal += x * x
        k -= x
        q = counts.index(x)
        # print(q)
        counts.remove(x)
        checked.remove(checked[q])
