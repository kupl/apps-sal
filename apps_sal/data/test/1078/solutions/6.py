n = int(input())

cnt = 0

for _ in range(n):
    v = int(input())
    if v % 2 == 0:
        print(v // 2)
    else:
        if cnt % 2 == 0:
            print(v // 2 + 1)
        else:
            print(v // 2)
        cnt += 1
