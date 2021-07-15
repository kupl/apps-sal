p, q, r = list(map(int, input().split()))

print((min(p+q, min(q+r, r+p))))

