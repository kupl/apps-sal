n = int(input())
ps = list(map(int, input().split()))
qs = input()
B = 0
for i in range(n):
    if qs[i] == 'B':
        B += ps[i]
maxi = B
b = B
for i in range(n):
    if qs[i] == 'A':
        b += ps[i]
    elif qs[i] == 'B':
        b -= ps[i]
    maxi = max(maxi, b)
b = B
for i in range(n - 1, -1, -1):
    if qs[i] == 'A':
        b += ps[i]
    elif qs[i] == 'B':
        b -= ps[i]
    maxi = max(maxi, b)
print(maxi)
