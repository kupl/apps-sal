a, b = input().split()
ab = int(a + b)

for j in range(ab):
    if j ** 2 <= ab:
        if j ** 2 == ab:
            print("Yes")
            return
    else:
        print("No")
        return
