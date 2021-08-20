def count_ones(x):
    ans = 0
    while x > 0:
        if x % 2 == 1:
            ans = ans + 1
        x = x // 2
    return ans


t = int(input())
for i in range(t):
    a = int(input())
    y = count_ones(a)
    print(2 ** y)
