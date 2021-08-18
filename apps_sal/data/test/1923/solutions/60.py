
list = []
for i in range(2):
    a = input()
    list.append(a)

N = list.pop(0)
s = list.pop(0)

stick_list = s.split()

stick_list.sort(key=int)

stick_list = [int(s) for s in stick_list]

sum = 0
for i in stick_list[::2]:
    sum = sum + i
print(sum)
