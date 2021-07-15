n, m, k = map(int, input().split())
r = []
for i in range(n):
    for j in range(m)[::-(i % 2) * 2 + 1]:
        r += [str(i+1), str(j+1)]

chunk = m*n//k
for i in range(k-1):
    print(chunk, ' '.join(r[2*i*chunk:2*(i+1)*chunk]))

print(len(r)- 2*(k-1)*chunk)//2, ' '.join(r[2*(k-1)*chunk:])
