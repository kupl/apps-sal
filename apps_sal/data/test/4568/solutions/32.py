N = int(input())
S = input()

print(max([len(set(list(S[:i])) & set(list(S[i:]))) for i in range(N)]))
