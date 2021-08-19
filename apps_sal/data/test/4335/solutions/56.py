n = int(input())
S = input()
if n % 2 == 1:
    print('No')
elif S[:n // 2] == S[n // 2:]:
    print('Yes')
else:
    print('No')
