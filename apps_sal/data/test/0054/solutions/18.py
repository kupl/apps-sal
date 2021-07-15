a, b = list(map(int, input().split(' ')))
if a == 2 or a == 3:
    print("YES")
    return

else:
    while b != 0:
        if b%a == 0:
            b //= a

        elif b%a == 1:
            b -= 1
            b //= a

        elif b%a == a-1:
            b += 1
            b //= a

        else:
            print("NO")
            return

print("YES")

