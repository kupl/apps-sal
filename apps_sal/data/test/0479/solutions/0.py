(n, k) = map(int, input().split())
a = set(map(int, input().split()))
q = int(input())
for _ in range(q):
    x = int(input())
    if x in a:
        print(1)
        continue
    found = False
    for i in range(2, k + 1):
        for j in range(1, i // 2 + 1):
            for l in a:
                t = x - l * j
                if t % (i - j) != 0:
                    continue
                if t // (i - j) in a:
                    print(i)
                    found = True
                    break
            if found:
                break
        if found:
            break
    if not found:
        print(-1)
