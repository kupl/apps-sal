n = int(input())
m = int(input())
k = sorted([int(input()) for i in range(n)])[::-1]
b = k[0]
s = 1
for i in range(1, n + 1):
    if b > m or b == m:
        print(s)
        break
    else:
        b += k[i]
        s += 1
