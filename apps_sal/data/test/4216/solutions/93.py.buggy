num = int(input())

digits = len(str(num))

ans = digits

for i in range(1, 10 ** (digits // 2 + 1)):
    if num % i == 0:
        target = max(len(str(i)), len(str(num // i)))
        if ans >= target:
            ans = target
        else:
            print(ans)
            return
print(ans)
