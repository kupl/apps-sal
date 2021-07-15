def calc(n):
    mod = 0
    for i in range(1, n+1):
        mod = mod *10
        mod = mod + 7
        mod = mod % n
        if mod == 0:
            return i
    return -1

k = int(input())
print(calc(k))
