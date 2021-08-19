K = int(input())
S = input()
print(S[:min(len(S), K)] + ('...' if len(S) > K else ''))
