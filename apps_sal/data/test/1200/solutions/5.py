n = int(input())

m = list(map(int, input().split()))

m.sort()

min_dif = m[1] - m[0] 

def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a %b)

for i in range(1, n):
    min_dif = nod(min_dif, m[i] - m[i-1])

ans = 0

for i in range(1, n):
    if m[i] - m[i-1] > min_dif:
        ans += (m[i] - m[i-1]) / min_dif - 1

print(int(ans))

