lst = input()
lst = lst.split()


for i in range(len(lst)):
    lst[i]= int(lst[i])
r = lst[0]
D = lst[1]
x = lst[2]

for i in range(10):
    x = r*x-D
    print(x)
