n = int(input())
aa = input().lower()
ab = input().lower()
ba = input().lower()
bb = input().lower()

mod = 10 ** 9 + 7
if n < 4:
    print((1))
    return

if ab == "b":
    if bb == "b":
        print((1))
    else:
        if ba == "a":
            print((pow(2, n - 3, mod)))
        else:
            dp_a = dp_b = 1
            for _ in range(n - 4):
                dp_a, dp_b = dp_b, (dp_a + dp_b) % mod
            print(((dp_a + dp_b) % mod))
else:
    if aa == "a":
        print((1))
    else:
        if ba == "b":
            print((pow(2, n - 3, mod)))
        else:
            dp_a = dp_b = 1
            for _ in range(n - 4):
                dp_a, dp_b = dp_b, (dp_a + dp_b) % mod
            print(((dp_a + dp_b) % mod))
