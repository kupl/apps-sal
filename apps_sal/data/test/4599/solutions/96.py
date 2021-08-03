N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

A = 0
B = 0
for i in range(N):
    if i % 2 == 0:
        A += a[i]
    else:
        B += a[i]

diff = A - B
print(diff)
