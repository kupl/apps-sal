import math
n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

b = []
count = 1
for i in range(n - 1):
    if(a[i] == a[i + 1]):
        count += 1
    else:
        b.append(count)
        count = 1
b.append(count)
flag = True
for i in b:
    if(i % 2):
        print('Conan')
        flag = False
        break
if(flag):
    print('Agasa')
