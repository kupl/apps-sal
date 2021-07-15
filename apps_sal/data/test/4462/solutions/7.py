N = int(input())
a = list(map(int, input().split()))

num2 = 0
num4 = 0
odd = 0
for i in a:
    if i % 4 == 0:
        num4 += 1
        continue
    elif i % 2 == 0:
        num2 += 1
        continue
    else:
        odd += 1
        continue
if odd<=num4 or (N%2==1 and num4==N//2):
    print('Yes')
else:
    print('No')

