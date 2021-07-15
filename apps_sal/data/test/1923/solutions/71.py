n = int(input())
l = list(map(int, input().split()))
l.sort()
num = 0
for i in range(0,2*n,2):
    num += min(l[i],l[i+1])
print(num)
