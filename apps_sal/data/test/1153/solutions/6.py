(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cur_a = 0
cur_b = 0
ia = 0
ib = 0
result = 0
while ia < n and ib < m:
    if cur_a < cur_b:
        cur_a += a[ia]
        ia += 1
    else:
        cur_b += b[ib]
        ib += 1
    if cur_a == cur_b:
        cur_a = 0
        cur_b = 0
        result += 1
while ia < n:
    cur_a += a[ia]
    ia += 1
    if cur_a == cur_b:
        cur_a = 0
        cur_b = 0
        result += 1
while ib < m:
    cur_b += b[ib]
    ib += 1
    if cur_a == cur_b:
        cur_a = 0
        cur_b = 0
        result += 1
print(result)
