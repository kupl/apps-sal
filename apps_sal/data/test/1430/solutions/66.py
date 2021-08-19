(N, K) = list(map(int, input().split(' ')))
S = input()
lengths = []
if S.startswith('0'):
    lengths.append(0)
cont = 0
for (s0, s1) in zip(S, S[1:] + 'x'):
    cont += 1
    if s0 != s1:
        lengths.append(cont)
        cont = 0
if S.endswith('0'):
    lengths.append(0)
window = 2 * K + 1
buf = sum(lengths[0:window])
ans = buf
for i in range(window, len(lengths)):
    buf += lengths[i]
    buf -= lengths[i - window]
    if i % 2 == 0:
        ans = max(ans, buf)
print(ans)
