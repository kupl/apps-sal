num = input().split()

N = int(num[0])
K = int(num[1])

S = input()

S2 = S[K-1]

S = S[:K-1] + S2.lower() + S[K:]

print(S)
