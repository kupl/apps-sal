n, a, b = map(int, input().split())
mas = list(map(int, input().split()))
count = 0
for i in range(n // 2):
    r, l = mas[i], mas[n - i - 1]
    if (mas[i] != mas[n - i - 1]) or mas[i] == 2:
        if r != 2 and l != 2:
            print(-1)
            return
        else:
            if r == 2 and l == 2:
                count += min(a, b) * 2
            else:
                if r == 0 or l == 0:
                    count += a
                else:
                    count += b

if n % 2 == 1:
    if mas[n // 2] == 2:
        count += min(a, b)
print(count)
