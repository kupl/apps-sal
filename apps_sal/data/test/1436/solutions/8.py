n = int(input())
A = list(map(int, input().split()))
c = 0
res = 0
for i in A:
    if i > 0:
        c += i
    elif c == 0:
        res += 1
    else:
        c -= 1
print(res)
