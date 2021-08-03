n = int(input())
if n == 1:
    print(0)
    return
if n == 2:
    print(1)
    return
print(n * (n - 1) // 2)
