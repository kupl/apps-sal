a, k = list(map(int, input().split()))
a = str(a)
i = 0
na = a
for q in range(len(a)):
    m = a[i]
    num = i
    for j in range(i, min(i + k + 1, len(a))):
        if a[j] > m:
            m = a[j]
            num = j
    na = ''
    for j in range(i):
        na += a[j]
    na += m
    for j in range(i + 1, num + 1):
        na += a[j - 1]
    for j in range(num + 1, len(a)):
        na += a[j]
    a = na
    k -= num - i
    i += 1
print(a)
    

