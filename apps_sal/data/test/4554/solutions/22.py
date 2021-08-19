lst = input().split()
W = int(lst[0])
a = int(lst[1])
b = int(lst[2])
if b - W <= a <= b + W:
    print(0)
else:
    print(max([b - (a + W), a - (b + W)]))
