S = input()
K = int(input())

substrings = set()
for length in range(1, K + 1):
    for i in range(len(S) - length + 1):
        substrings.add(S[i:i + length])

substrings = sorted(substrings)

print((substrings[K - 1]))

