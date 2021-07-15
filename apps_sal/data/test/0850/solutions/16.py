n = int(input())
v = list(map(int, input().split()))

cnt = [0]*101
ans = list()

v.sort()

f10 = 0
f100 = 0
for x in v:
    if x == 0 or x == 100:
        ans.append(x)
    elif x < 10:
        if f10 == 0:
            ans.append(x)
        f10 = 1
    elif x % 10 == 0:
        if f100 == 0:
            ans.append(x)
        f100 = 1

if f10 + f100 == 0:
    for i in range(1, 100):
        if i in v:
            ans.append(i)
            break
print(len(ans))
for i in ans:
    print (i, end=' ')



