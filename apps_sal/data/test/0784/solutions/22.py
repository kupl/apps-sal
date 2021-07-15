a, b = map(int, input().split())
flag = True
order = [b]
while b > a:
    if b % 2 == 0:
        b //= 2
        order.append(b)
    elif b % 10 == 1:
        b //= 10
        order.append(b)
    else:
        break
if b == a:
    print("YES")
    print(len(order))
    for i in range(len(order) - 1, -1, -1):
        print(order[i], end=" ")
else:
    print("NO")
