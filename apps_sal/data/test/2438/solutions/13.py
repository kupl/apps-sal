n = int(input())
a = list(input())
A = B = -1
index = [0] * n
arr = 0
is_a = -1
is_b = -1
for i in range(n - 1, -1, -1):
    if a[i] == 'A':
        index[i] = A
        if A == -1:
            is_a = i
        A = i
    else:
        index[i] = B
        if B == -1:
            is_b = i
        B = i
for i in range(n):
    if index[i] - 1 == i:
        if a[i] == 'A':
            if is_b >= i:
                arr -= 1
        else:
            if is_a >= i:
                arr -= 1
    if index[i] != -1:
        arr += n - index[i]

print(arr)
