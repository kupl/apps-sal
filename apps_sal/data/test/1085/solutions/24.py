N = int(input())

divs = set()
n = 1
while n * n <= N:
    if N % n == 0:
        divs.add(n)
        divs.add(N // n)
    n += 1

divs2 = set()
n = 1
while n * n <= (N - 1):
    if (N - 1) % n == 0:
        divs2.add(n)
        divs2.add((N - 1) // n)
    n += 1

ans = len(divs2) - 1
for d in divs:
    if d == 1:
        continue
    n = N
    while n >= 1:
        if n == 1:
            ans += 1
            break
        if n % d == 0:
            n //= d
        else:
            if n % d == 1:
                ans += 1
            break

print(ans)
