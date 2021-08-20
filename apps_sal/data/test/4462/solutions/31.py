import math
N = int(input())
A = list(map(int, input().split()))
count = []
for i in A:
    if i % 4 == 0:
        count.append('4')
    elif i % 2 == 0:
        count.append('2')
    else:
        count.append('1')
B1 = count.count('4')
B2 = count.count('1')
if count.count('2') == 0:
    print('Yes' if B1 + 1 >= B2 else 'No')
else:
    print('Yes' if B1 >= B2 else 'No')
