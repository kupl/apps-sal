n = int(input())

for i in range(n):
    name, before, after = input().split()
    before = int(before)
    after = int(after)
    if before < after:
        if after >= 2400 and before >= 2400:
            print('YES')
            return
print('NO')
