(n, x) = list(map(int, input().split()))
L = list(map(int, input().split()))
ans = 0
ct = 1
for i in range(n):
    ans = ans + L[i]
    if ans > x:
        break
    else:
        ct += 1
print(ct)
