
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

s = int(input())
a = 1
for i in p:
    if s % i == 0:
        a = i
        break
print(str(a) + str(s // a))
