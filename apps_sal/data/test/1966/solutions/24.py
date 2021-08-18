
def bubble_sort(a_list):
    changed = True
    while changed:
        changed = False
        for i in range(len(a_list) - 1):
            if a_list[i] > a_list[i + 1]:
                changed = True
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
    return a_list


n = int(input())

str1 = ''
for i in range(n):

    str1 = str1 + input()
j = input()
str2 = ''
for i in range(n):

    str2 = str2 + input()
j = input()
str3 = ''
for i in range(n):

    str3 = str3 + input()
str4 = ''
j = input()
for i in range(n):

    str4 = str4 + input()

str1comp = "01" * (n**2)

a = 0
b = 0
c = 0
d = 0


for i in range(n**2):
    if str1[i] == str1comp[i]:
        a += 1
for i in range(n**2):
    if str2[i] == str1comp[i]:
        b += 1
for i in range(n**2):
    if str3[i] == str1comp[i]:
        c += 1
for i in range(n**2):
    if str4[i] == str1comp[i]:
        d += 1

lst2 = []
lst2.append(a)
lst2.append(b)
lst2.append(c)
lst2.append(d)


bubble_sort(lst2)


sum3 = 0

for i in range(2):
    sum3 += lst2[i]
for i in range(2, 4):
    sum3 += (n**2 - lst2[i])

print(sum3)
