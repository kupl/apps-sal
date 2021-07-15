lis = list(map(int,input().split()))
a = int(input())
lis.sort(reverse = True)
for i in range(a):
    lis[0] *= 2
print(sum(lis))
