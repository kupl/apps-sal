n = int(input())
maxx = 1
x = input().split()
A = [x]
res = 1
for i in range(n - 1):
    y = input().split()
    if y == A[-1]:
        res += 1
    else:
        res = 1
    A.append(y)
    if res > maxx:
        maxx = res
print(maxx)
