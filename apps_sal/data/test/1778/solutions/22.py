n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
s_a = s_b = 0
a_j = b_j = n - 1
for i in range(2 * n):
    if i % 2 == 0:
        if a_j == -1:
            b_j -= 1
        elif b_j == -1:
            s_a += a[a_j]
            a_j -= 1
        elif a[a_j] < b[b_j]:
            b_j -= 1
        else:
            s_a += a[a_j]
            a_j -= 1
    elif b_j == -1:
        a_j -= 1
    elif a_j == -1:
        s_b += b[b_j]
        b_j -= 1
    elif b[b_j] < a[a_j]:
        a_j -= 1
    else:
        s_b += b[b_j]
        b_j -= 1
print(s_a - s_b)
