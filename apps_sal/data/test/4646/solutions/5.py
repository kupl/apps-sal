tests = int(input())
for _ in range(tests):
    n = int(input())
    sp = list(map(int, input().split()))
    ch = 0
    for i in sp:
        if i % 2 == 0:
            ch += 1
    if ch != n - n // 2:
        print(-1)
        continue
    count = 0
    for i in range(n):
        if i % 2 != sp[i] % 2:
            count += 1
    print(count // 2)
