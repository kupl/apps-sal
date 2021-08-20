x = int(input())
(ans1, mod) = divmod(x, 11)
if mod == 0:
    print(ans1 * 2)
elif 1 <= mod <= 6:
    print(ans1 * 2 + 1)
else:
    print(ans1 * 2 + 2)
