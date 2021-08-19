N = int(input())
S = input()
print('Yes' if N % 2 == 0 and S[0:N // 2] == S[N // 2:N] else 'No')
