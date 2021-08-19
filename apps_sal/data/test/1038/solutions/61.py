(a, b) = list(map(int, input().split()))
n = len(bin(b)[2:])
ans = [0] * n
for i in range(n):
    value = 2 ** i
    total = 0
    if not a // value == b // value:
        if a // value % 2 == 0:
            start = a // value + 1
        else:
            total += value - a % value
            start = a // value + 2
        if b // value % 2 == 0:
            end = b // value - 1
        else:
            total += b % value + 1
            end = b // value - 2
        if start == end:
            total += value
        elif start > end:
            pass
        else:
            total += ((end - start + 1) // 2 + 1) * value
    elif a // value % 2 == 1:
        total = b - a + 1
    ans[n - i - 1] = total % 2
print(int(''.join(map(str, ans)), 2))
