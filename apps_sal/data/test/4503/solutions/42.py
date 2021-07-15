
H, N = map(int, input().split())
A = list(map(int, input().split()))

Total_attack = sum(A)

if H - Total_attack <= 0:
    print('Yes')

else:
    print('No')
