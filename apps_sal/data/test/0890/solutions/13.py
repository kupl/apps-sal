n, l, r, x = map(int, input().split())
a = input().split()
ran = 2**n
answer = 0
for i in range(n):
    a[i] = int(a[i])
for i in range(ran):
    m = i
    mask = ""
    while m != 0:
        if m % 2 == 0:
            mask += '0'
        else:
            mask += '1'
        m = m // 2
    while len(mask) < n:
        mask += '0'
    s = 0
    easy = 10**9 + 100
    hard = 0
    for j in range(len(mask)):
        if mask[j] == '1':
            if a[j] >= hard:
                hard = a[j]
            if a[j] <= easy:
                easy = a[j]
            s += a[j]
    if s <= r and s >= l and hard - easy >= x:
        answer += 1

print(answer)
