n = int(input())
r = [int(i) for i in input().split()]
for i in range(1,n):
    r[i] += r[i-1]

a = r.copy()
ans_a = 0; change_v = 0
for i in range(n):
    a[i] += change_v
    if i%2 == 1:
        ans_a += max(0,1-a[i])
        change_v += max(0,1-a[i])
    else:
        ans_a += max(0,a[i]+1)
        change_v -= max(0,a[i]+1)

a = r.copy()
ans_b = 0; change_v = 0
for i in range(n):
    a[i] += change_v
    if i%2 == 0:
        ans_b += max(0,1-a[i])
        change_v += max(0,1-a[i])
    else:
        ans_b += max(0,a[i]+1)
        change_v -= max(0,a[i]+1)

print((min(ans_a,ans_b)))

