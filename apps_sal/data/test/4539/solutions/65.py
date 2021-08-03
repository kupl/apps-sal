N = int(input())
X = 0
for i in str(N):
    X += int(i)

if N % X == 0:
    print('Yes')
else:
    print('No')
