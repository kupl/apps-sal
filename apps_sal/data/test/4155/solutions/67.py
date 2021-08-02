n = int(input())
hh = list(map(int, input().split()))
cnt = 0

while hh.count(0) != n:
    a = [i for i, x in enumerate(hh) if x == 0]

    if a != []:
        for i in range(len(a) - 1):
            if a[i] + 1 != a[i + 1]:
                for j in range(a[i] + 1, a[i + 1]):
                    hh[j] -= 1
                cnt += 1

        if a[0] != 0:
            for j in range(a[0]):
                hh[j] -= 1
            cnt += 1

        if a[-1] != n - 1:
            for j in range(a[-1] + 1, n):
                hh[j] -= 1
            cnt += 1

    else:
        for i in range(n):
            hh[i] -= 1
        cnt += 1

print(cnt)
