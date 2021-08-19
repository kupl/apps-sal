(q, w, e) = list(map(int, input().split()))
i = 1
q *= 10
while q // w != e:
    q %= w
    q *= 10
    i += 1
    if i > 1000:
        i = -1
        break
print(i)
