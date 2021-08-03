n, ln = [i for i in input().split(' ')]

ans = n[0]

i = 1

while i < len(n) and n[i] < ln[0]:
    ans += n[i]
    i += 1

ans += ln[0]
print(ans)
