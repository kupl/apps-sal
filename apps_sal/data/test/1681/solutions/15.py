colour = input()
new_colour = input()
sum = 0
k = 0
list = []
for i in new_colour:
    if i not in list:
        list += i
for i in list:
    a = colour.count(i)
    b = new_colour.count(i)
    if a > b:
        sum += b
    else:
        sum += a
    if i not in colour:
        k += 1
if k > 0:
    print(-1)
else:
    print(sum)
