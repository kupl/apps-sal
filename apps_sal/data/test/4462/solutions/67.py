N = int(input())
A = list(map(int, input().split()))
mod0 = 0
mod2 = 0
mod13 = 0
for a in A:
    mod = a % 4
    if mod == 0:
        mod0 += 1
    elif mod == 2:
        mod2 += 1
    else:
        mod13 += 1
if mod2 > 0:
    if mod13 <= mod0:
        print('Yes')
    else:
        print('No')
elif mod13 - 1 <= mod0:
    print('Yes')
else:
    print('No')
