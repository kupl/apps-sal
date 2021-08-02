n, m = [int(n) for n in input().split()]
a = sorted([int(n) for n in input().split()])

ans = 0
if m > sum(a):
    ans = -1
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            fold = j // i
            amari = j % i
            suma = sum(a[-1 * j:]) - ((fold - 1) * fold // 2) * i - amari * fold
            if suma >= m:
                ans = i
                break
        if ans > 0:
            break

print(ans)
