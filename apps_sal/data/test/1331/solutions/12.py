(n, m, k) = list(map(int, input().split()))
clock = list(map(int, input().split()))
clock.sort()
unlock = [1] * n
count = 0
j = 0
if k == 1:
    count = n
else:
    for i in range(n):
        while clock[i] - clock[j] >= m:
            k += unlock[j]
            j += 1
        k -= 1
        if k < 1:
            count += 1
            k = 1
            unlock[i] = 0
print(count)
