S = int(input())
N = input()
print('Yes' if N[:S // 2] == N[S // 2:] else 'No')
