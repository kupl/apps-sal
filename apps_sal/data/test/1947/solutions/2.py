n, m, l = list(map(int, input().split()))
a = input().split()
b = [0] * n
for i in range(n):
    b[i] = int(a[i])
count = 0
for i in range(n):
    if b[i] > l:
        count += 1
        if i > 0:
            if b[i - 1] > l:
                count -= 1
for i in range(m):
    t = input().split()
    if int(t[0]) == 0:
        print(count)
    else:
        p = int(t[1])
        d = int(t[2])
        if b[p - 1] <= l:
            b[p - 1] += d
            if b[p - 1] > l:
                if n == 1:
                    count += 1
                else:
                    if p - 1 > 0 and p - 1 < n - 1:
                        if b[p - 2] > l and b[p] > l:
                            count -= 1
                        elif b[p - 2] <= l and b[p] <= l:
                            count += 1
                    elif p - 1 == n - 1:
                        if b[p - 2] <= l:
                            count += 1
                    else:
                        if b[p] <= l:
                            count += 1
