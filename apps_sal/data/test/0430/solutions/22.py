y = input()
x = input()
list = []
n = 0
while n < len(x):
    list.append(x[n:n + 3])
    n += 4
a = list.count('100')
b = list.count('200')
fair = 'YES'
if a % 2 == 1:
    fair = 'NO'
if a == 0:
    if b % 2 == 1:
        fair = 'NO'
print(fair)
