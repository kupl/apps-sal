N = int(input())
otoshidama = 0
for i in range(N):
    x, u = input().split()

    if u == 'JPY':
        otoshidama += int(x)
    else:
        otoshidama += float(x) * 380000

print(otoshidama)
