def f(x):
    x1 = len(x)
    x1 = '1' * x1
    return x1


n = int(input())
for i in range(n):
    a = input()
    ans = ((len(a) - 1) * 9)
    a1 = f(a)
    a1, a = int(a1), int(a)
    ans += a // a1
    print(ans)
