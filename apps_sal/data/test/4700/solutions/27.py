N, M = list(map(int, input().split()))
list_h = list(map(int, input().split()))
table = [1] * N

for i in range(M):
    A, B = list(map(int, input().split()))
    if list_h[B - 1] < list_h[A - 1]:
        table[B - 1] = 0
    elif list_h[A - 1] < list_h[B - 1]:
        table[A - 1] = 0
    else:
        table[A - 1] = 0
        table[B - 1] = 0

print(str(sum(table)))
