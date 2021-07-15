N = int(input())
data = list(map(int,input().split()))

max = 0
kei = 0

for i in range(len(data)):
    kei += data[i]
    if max < data[i]:
        max = data[i]

if max < kei - max:
    print('Yes')
else:
    print('No')
