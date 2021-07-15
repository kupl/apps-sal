n = int(input())
a = list(map(int, input().split()))

S = a[0] + a[1]
C = 0
for i in range(2, n):
    C ^= a[i]

D = S - C

if D < 0 or D % 2 == 1:
    print(-1)
    return

D //= 2

ans = 0

free_keta = []

for i in range(100):
    if (C & (1 << i)) != 0:
        free_keta.append(i)
        if (D & (1 << i)) != 0:
            print(-1)
            return
    else:
        ans += (D & (1 << i))

if ans > a[0]:
    print(-1)
    return
        
for keta in free_keta[::-1]:
    if ans + (1 << keta) <= a[0]:
        ans += (1 << keta)

if ans == 0:
    print(-1)
    return
    
print(a[0] - ans)
