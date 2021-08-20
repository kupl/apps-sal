N = int(input())
list1 = list(map(int, input().split()))
list1.sort()
x = list1[0]
y = list1[-1]
s = 0
list2 = []
while x + s <= y:
    list2.append(x + s)
    s = s + 1
list3 = []
for j in list2:
    w = 0
    for i in list1:
        w = w + (i - j) * (i - j)
    list3.append(w)
list3.sort()
print(list3[0])
