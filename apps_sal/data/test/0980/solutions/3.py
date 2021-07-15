import sys

k, n = list(map(int, input().split()))
s = [list(word.rstrip()) for word in sys.stdin]

double = True if max(s[0].count(chr(i+97)) for i in range(26)) > 1 else False
diff = [set() for _ in range(k)]
diff_cnt = [0]*k
for i in range(1, k):
    for j in range(n):
        if s[0][j] != s[i][j]:
            diff[i].add(j)
            diff_cnt[i] += 1
            if diff_cnt[i] > 4:
                print(-1)
                return

for i in range(n):
    for j in range(i+1, n):
        s[0][i], s[0][j] = s[0][j], s[0][i]
        for x in range(1, k):
            w = [y for y in diff[x] | {i, j} if s[0][y] != s[x][y]]
            if double and len(w) == 0:
                continue
            if len(w) == 2 and s[0][w[0]] == s[x][w[1]] and s[0][w[1]] == s[x][w[0]]:
                continue
            break
        else:
            print(''.join(s[0]))
            return
        s[0][i], s[0][j] = s[0][j], s[0][i]

print(-1)

