N = int(input())
S = input().split()
print('Three' if len(set(S)) & 1 else 'Four')
