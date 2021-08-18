a, b, x = map(int, input().split())
arr = [0]

if x >= a * (10**9) + b * 10:
    print(10**9)
    return

elif x < a + b:
    print(0)
    return

else:
    for i in range(1, 10):
        n = (x - b * i) // a
        if len(str(n)) > i:
            arr.append(10**i - 1)
        else:
            arr.append(n)

    print(max(arr))
