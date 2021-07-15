N, M = list(map(int, input().split()))
S = input().split('*')
T = input()

if (len(S) == 1):
  print("YES" if S[0] == T else "NO")
else:
  print("YES" if S[0] == T[:len(S[0])] and S[1] == T[len(T) - len(S[1]):] and len(S[0]) + len(S[1]) <= len(T) else "NO")

