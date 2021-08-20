n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    ans = 0
    num_1 = 2
    num_2 = 1
    for i in range(n - 1):
        ans = num_1 + num_2
        (num_1, num_2) = (num_2, ans)
    print(ans)
