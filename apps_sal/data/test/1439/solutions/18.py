n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
rem = set()
for i in a:
    new = {(i + j) % m for j in rem | {0}}
    rem |= new
    if 0 in rem:
        print('YES')
        return
print('NO')

