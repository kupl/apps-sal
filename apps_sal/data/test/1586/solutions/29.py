n = input()
m = len(n)
n = int(n)
if n % 2 == 1:
    print(0)
elif m == 1:
    print(0)
else:
    ans = 0
    i = 1
    while True:
        ans_plus = n // (2 * 5 ** i)
        if ans_plus == 0:
            break
        ans += ans_plus
        i += 1
    print(ans)
