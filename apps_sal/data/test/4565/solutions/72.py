n = int(input())
s = input()
total_E = s.count('E')
total_W = n - total_E
right_E = []
tmp_E = total_E
tmp_W = 0
for i in range(n):
    if s[i] == 'E':
        tmp_E -= 1
    right_E.append(tmp_E)
left_W = [0]
for i in range(1, n):
    if s[i - 1] == 'W':
        tmp_W += 1
    left_W.append(tmp_W)
candidates = []
for i in range(n):
    candidates.append(right_E[i] + left_W[i])
ans = min(candidates)
print(ans)
