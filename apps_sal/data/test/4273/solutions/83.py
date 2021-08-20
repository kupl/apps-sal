n = int(input())
s_l = [input() for _ in range(n)]
name_d = ['M', 'A', 'R', 'C', 'H']
sub_s = {}
for d in name_d:
    sub_s[d] = 0
for s in s_l:
    if s[0] in name_d:
        sub_s[s[0]] += 1
ans = 0
memo = set()
for i in range(5):
    for j in range(5):
        for k in range(5):
            (a, b, c) = sorted([i, j, k])
            if a != b and a != c and (b != c):
                key = str(a) + str(b) + str(c)
                if key not in memo:
                    ans += sub_s[name_d[a]] * sub_s[name_d[b]] * sub_s[name_d[c]]
                    memo.add(key)
print(ans)
