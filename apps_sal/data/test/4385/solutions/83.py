a = []
for i in range(5):
    a.append(int(input()))
a.sort()
j = int(input())
k = a[4] - a[0]
if k <= j:
    print("Yay!")
else:
    print(":(")
