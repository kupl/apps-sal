N, K, C = list(map(int, input().split()))
S = input()
length = len(S)

INF = float('inf')
Ls = [-INF]
n = 0
for i, c in enumerate(S):
    if c == 'o' and i - Ls[-1] > C:
        Ls.append(i)
        n += 1
        if n >= K: break

Rs = [INF]
n = 0
for i, c in enumerate(reversed(S)):
    if c == 'o' and Rs[-1] - (length-1-i) > C:
        Rs.append(length-1-i)
        n += 1
        if n >= K: break
Rs.reverse()

for l, r in zip(Ls[1:], Rs[:-1]):
    if l == r:
        print((l+1))

