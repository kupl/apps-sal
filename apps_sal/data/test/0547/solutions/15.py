parse_int = lambda: list(map(int, input().split()))

n,k = parse_int()

passw = set()
for _ in range(n): passw.add(input().strip())
passw = [len(el) for el in passw]
passw.sort()

tru = len(input().strip())

time = 0
before_shtraf = k
lucky, unlucky = 999999999, 0
for el in passw:
    time += 1

    if el == tru:
        lucky = min(lucky, time)
        unlucky = time

    before_shtraf -= 1
    if before_shtraf <= 0:
        before_shtraf = k
        time += 5

print(lucky, unlucky)
