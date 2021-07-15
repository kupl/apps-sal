n,m = map(int,input().split())
li = list(map(int,input().split()))
li.sort(reverse=True)

sum = 0
cnt = 0
for i in li:
    sum += i


if li[m-1]*4*m >= sum:
    print('Yes')
else:
    print('No')
