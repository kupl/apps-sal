(N, S) = input().split()
N = int(N) + 1
ans = 0
for i in range(N):
    counts = {base: 0 for base in 'ATGC'}
    for j in range(i + 2, N, 2):
        counts[S[j - 2]] += 1
        counts[S[j - 1]] += 1
        if counts['A'] == counts['T'] and counts['G'] == counts['C']:
            ans += 1
print(ans)
