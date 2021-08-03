n, m = list(map(int, input().split()))
ln = []
lm = []

for i in range(n):
    ln.append(input())
for i in range(m):
    lm.append(input())

lim = n - m + 1
for i in range(lim):
    for j in range(lim):
        l = 0
        for k in ln[i:i + m]:
            if k[j:j + m] != lm[l]:
                break
            l += 1
        else:
            print("Yes")
            break
    else:
        continue
    break

else:
    print("No")
