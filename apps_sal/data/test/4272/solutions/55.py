N = int(input())
S = input()

count = 0

for i in range(len(S) - 3 + 1):
    if S[i] + S[i + 1] + S[i + 2] == 'ABC':
        count += 1

print(count)
