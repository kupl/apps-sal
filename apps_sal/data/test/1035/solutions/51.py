import math
A, B = map(int, input().split())


def fact(x):
    temp = x
    arr = [1]
    for i in range(2, int(math.sqrt(x))):
        if temp % i == 0:
            c = 0
            while temp % i == 0:
                c += 1
                temp //= i
            arr.append(i)
    if temp != 1:
        arr.append(temp)
    if arr == []:
        arr.append(n)
    return arr


a = fact(A)
b = fact(B)
ans = 0
for i in a:
    if i in b:
        ans += 1


print(ans)
