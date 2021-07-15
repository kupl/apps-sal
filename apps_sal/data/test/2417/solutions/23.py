n = int(input())


a = list(map(int, input().split()))
dictt = {}
for x in range(n):
    dictt[a[x]] = x
# print(dictt)
b = list(map(int, input().split()))
bb = []
for x in b:
    bb.append(dictt[x])
# print(bb)
bb.reverse()
# work with bb
fines = 0
smallest = bb[0]
largest = bb[0]
for i in range(1, n):
    if bb[i] > smallest:
        fines += 1
        # print(f"xx{i}")
    if bb[i] > largest:
        largest = bb[i]
    if bb[i] < smallest:
        smallest = bb[i]
print(fines)

