string = list(input())
n = len(string)
asubsets = []
a = 0
b = 1
for i in range(n):
    if string[i] == 'a':
        a = a + 1
    if string[i] == 'b':
        asubsets.append(a)
        a = 0
asubsets.append(a)
increase = [i + 1 for i in asubsets]
total = 1
for i in increase:
    total = total * i
finaltotal = (total - 1) % (pow(10, 9) + 7)
print(finaltotal)
