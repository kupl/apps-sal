N = int(input())
S = input()
if N % 2 == 1:
    print('No')
else:
    ans = 'Yes' if S[:N // 2] == S[N // 2:] else 'No'
    print(ans)
