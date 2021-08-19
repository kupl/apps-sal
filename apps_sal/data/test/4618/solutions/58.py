s = str(input())
K = int(input())
substrings = set([])
for i in range(5):
    for j in range(len(s) - i):
        substrings.add(s[j:j + i + 1])
print(sorted(substrings)[K - 1])
