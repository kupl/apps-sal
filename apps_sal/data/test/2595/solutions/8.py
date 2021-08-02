t = int(input())

for _ in range(t):
    a, b = list(map(int, input().strip().split()))
    a, b = min(a, b), max(a, b)
    if b % a != 0:
        print(-1)
    else:
        cnt = 0
        while a < b:
            a *= 2
            cnt += 1
        if a > b:
            print(-1)
        else:
            result = cnt // 3
            if cnt % 3 >= 1:
                result += 1
            print(result)
