(n, m, k) = map(int, input().split())
best = 1
sleva = k - 1
sprava = n - k
m -= n
put = 1
while m >= put:
    m -= put
    best += 1
    put += (sleva > 0) + (sprava > 0)
    if sleva:
        sleva -= 1
    if sprava:
        sprava -= 1
    if sleva == sprava == 0:
        best += m // put
        break
print(best)
