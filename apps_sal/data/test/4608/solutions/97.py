N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
x = 1
Sum = 0
while x != 2 and Sum < N:
    x = a[x - 1]
    Sum += 1
if Sum >= N:
    print(-1)
else:
    print(Sum)
