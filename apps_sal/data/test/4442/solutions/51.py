(a, b) = map(int, input().split())
list = []
if a > b:
    for i in range(a):
        list.append(b)
else:
    for j in range(b):
        list.append(a)
list = [str(a) for a in list]
list = ''.join(list)
print(list)
