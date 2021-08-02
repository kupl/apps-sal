a, b = list(map(int, input().split()))
q = input()
p = ""

for i in range(0, b):
    j = 0
    while j <= len(q) - 2:
        if q[j] == 'B' and q[j + 1] == 'G':
            p = p + "GB"
            j = j + 2
        else:
            p = p + q[j]
            j = j + 1
    if j == len(q) - 1:
        p = p + q[j]
    q = p
    p = ""

print(q)
