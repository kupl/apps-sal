
N = int(input())
A = list(map(int, input().split()))


num = 1
for i in A:
    if i == num:
        num += 1
if num == 1:
    print((-1))
else:
    print((N - (num - 1)))
