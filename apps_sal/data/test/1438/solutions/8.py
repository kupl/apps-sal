n, k = list(map(int, input().split()))
a = (list(map(int, input().split())))
b = (list(map(int, input().split())))
c = list(zip(a, b))
c.sort(key=lambda x: (x[1] // x[0]))
i = 0
count = c[0][1] // c[0][0]
part = 0
full = 0
while k > 0 and i < n:
    if count < c[i][1] // c[i][0]:
        if k > part:
            k -= part
            part = 0
            count += 1
            dco = min(c[i][1] // c[i][0] - count, k // full)
            count += dco
            k -= dco * full
            part = full + c[i][0] - c[i][1] % c[i][0]
            full += c[i][0]
        else:
            break
    else:
        part += c[i][0] - c[i][1] % c[i][0]
        full += c[i][0]
    #~ print(part, full)
    i += 1
if k > part:
    count += 1
    k -= part
count += k // full
print(count)
