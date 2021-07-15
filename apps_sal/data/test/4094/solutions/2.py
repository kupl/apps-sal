k = int(input())

if 7 % k == 0:
    print(1)
    return

a = [7 % k]
for i in range(2, k+1):
    aa = (10 % k) * a[-1] + a[0]
    a.append(aa % k)
    if a[-1] % k == 0:
        print(i)
        return

print(-1)
