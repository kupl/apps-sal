__author__ = 'kolya'
n = int(input())
m = [int(i) for i in input().split()]

counter = 1
max = 1
f = m[0]
for i in range(1, n):
    if m[i] >= f:
        counter += 1
    else:
        if counter > max:
            max = counter
        counter = 1
    f = m[i]
if(counter > max):
    max = counter
print(max)
