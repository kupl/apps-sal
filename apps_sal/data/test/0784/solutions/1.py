a, b = list(map(int, input().split()))
k = [b]
f = 1
while b > a:
    if (b % 10 == 1):
        b -= 1
        b //= 10
    elif (b % 2 == 0):
        b //= 2
    else:
        f = 0
        break
    k.append(b)
else:
    k.reverse()
    if (k[0] == a):
        print("YES")
        print(len(k))
        print(*k)
    else:
        print("NO")
if f == 0:
    print("NO")
