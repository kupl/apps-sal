num = int(input())
t = [int(n) for n in input().split()]
t = sorted(t)

valid = True

if num % 2 == 1:  # odd
    check = list(range(0, num + 1, 2))[1:]

    valid1 = t[0] == 0
    valid2 = check == t[2::2]  # even, skip first
    valid3 = check == t[1::2]  # odd
    valid = valid1 and valid2 and valid3

    if not valid:
        print((0))
    else:
        ans = 2**((num - 1) // 2) % (10**9 + 7)
        print(ans)

else:  # even
    check = list(range(1, num, 2))

    valid1 = True
    valid2 = check == t[::2]  # even
    valid3 = check == t[1::2]  # odd
    valid = valid1 and valid2 and valid3

    if not valid:
        print((0))
    else:
        ans = 2**((num) // 2) % (10**9 + 7)
        print(ans)
