import math
S = input()
r = len(S)
z = 0
str_list = []
while z < r:
    str_list.append(S[z])
    z = z + 1

N = len(str_list)
x = math.floor((N - 1) / 2)
y = math.floor((N + 3) / 2)

s = 0

list1 = str_list[::-1]

if list1 == str_list:
    s = s + 1

list2 = []
list3 = []

t = 0
while t < x:
    list2.append(str_list[t])
    t = t + 1

list4 = list2[::-1]
if list2 == list4:
    s = s + 1

u = y - 1
while u < N:
    list3.append(str_list[u])
    u = u + 1

list5 = list3[::-1]
if list3 == list5:
    s = s + 1


if s == 3:
    print('Yes')
else:
    print('No')
