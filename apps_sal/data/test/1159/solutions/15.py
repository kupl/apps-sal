n = int(input())
l = [(i, i + 1) for i in range(1, n)]
l.append((n, 1))
cnt = n


def is_prime(k):
    j = 2
    while j * j <= k:
        if k % j == 0:
            return False
        j += 1
    return True


for i in range(1, n - 1):
    if is_prime(cnt):
        break
    cnt += 1
    l.append((i, n - i))
print(cnt)
for i in l:
    print(i[0], i[1])
