n = int(input())
lis = list(map(int, input().split()))

minus = 0
for i in range(n):
    if lis[i] < 0:
        minus += 1
        lis[i] = lis[i]*-1

if 0 in lis or minus % 2 == 0:
    print(sum(lis))
else:
    print(sum(lis) - 2*min(lis))
