n = int(input())
for _ in range(n):
    l = input().split()
    before = int(l[1])
    after = int(l[2])
    if 2400 <= before < after:
        print('YES')
        break
else:
    print('NO')
