a, b, c = list(map(int, input().split()))
for i in range(1, 2*b+1):
    if i*a%b == c:
        print('YES')
        return
print('NO')

