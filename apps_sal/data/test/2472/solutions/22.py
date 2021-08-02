c = D = 0
for b, a in sorted([tuple(map(int, input().split()))[::-1] for _ in range(int(input()))]):
    c += a
    D |= b < c
print('No' if D else 'Yes')
