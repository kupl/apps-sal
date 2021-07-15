from collections import Counter

N = int(input())
S = [input()[:1] for _ in range(N)]
c = Counter(S)

first_name = 'MARCH'
c = [c[i] for i in first_name if c[i]]

ans = 0
if len(c) > 2:
    ans += c[0]*c[1]*c[2]

if len(c) > 3:
    for i in c[3:]:
        for j in range(3):
            tmp = c[:3]
            tmp[j] = i
            ans += tmp[0]*tmp[1]*tmp[2]
if len(c) > 4:
    tmp = c[3:]
    for j in range(3):
        ans += tmp[0]*tmp[1]*c[j]
print(ans)
