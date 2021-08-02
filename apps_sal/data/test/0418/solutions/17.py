N = int(input())
for i in range(N):
    S, b, a = input().split()
    b, a = (int(n) for n in (b, a))
    if b >= 2400 and a > b:
        print('YES')
        break
else:
    print('NO')
