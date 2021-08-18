n = int(input())


a = list(map(int, input().split()))
dictt = {}
for x in range(n):
    dictt[a[x]] = x
b = list(map(int, input().split()))
bb = []
for x in b:
    bb.append(dictt[x])
bb.reverse()
fines = 0
smallest = bb[0]
largest = bb[0]
for i in range(1, n):
    if bb[i] > smallest:
        fines += 1
    if bb[i] > largest:
        largest = bb[i]
    if bb[i] < smallest:
        smallest = bb[i]
print(fines)
