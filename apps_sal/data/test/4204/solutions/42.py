S = input()
K = int(input())

i = 0
while i < len(S) and S[i] == '1':
    i += 1

if i >= K:
    print(1)
else:
    print(S[i])
