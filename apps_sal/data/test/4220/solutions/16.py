K = int(input())
S = input()
N = len(S)

print(S[:K] + "..." if len(S) > K else S)
