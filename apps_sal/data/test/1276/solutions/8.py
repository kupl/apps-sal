n = int(input())
s = input()
D = {'R': [], 'G': [], 'B': []}
for i in range(1, n + 1):
    D[s[i - 1]].append(i)
ans = len(D['R']) * len(D['G']) * len(D['B'])
count = 0
for i in range(0, n):
    for j in range(i + 1, n):
        k = 2 * j - i
        if k >= n:
            break
        if s[i] != s[j] and s[j] != s[k] and (s[i] != s[k]):
            count += 1
print(ans - count)
