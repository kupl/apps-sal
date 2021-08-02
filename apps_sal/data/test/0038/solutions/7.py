import sys
N, L = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for shift in range(N):
    coincide = True
    diff = b[shift] - a[0]
    for i in range(1, N):
        if (a[i] + diff) % L != b[(i + shift) % N]:
            coincide = False
            break
    if coincide:
        print("YES")
        return

print("NO")
