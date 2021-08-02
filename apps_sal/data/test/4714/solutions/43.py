a, b = list(map(int, input().split()))
cnt = 0

for i in range(a, b + 1):
    lis_i = list(str(i))
    lis_i.reverse()
    rev_i = int(''.join(lis_i))
    if rev_i == i:
        cnt += 1

print(cnt)
