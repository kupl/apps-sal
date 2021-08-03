N = int(input())
ans = False

for i in range(1, 10):
    for j in range(1, 10):
        if N == i * j:
            ans = True

if ans == True:
    print('Yes')
else:
    print('No')
