(N, M) = list(map(int, input().split()))
name = input()
table = [0] * 26
for i in range(26):
    table[i] = i
buffs = []
for _ in range(M):
    (before, after) = list(map(ord, input().split()))
    before -= ord('a')
    after -= ord('a')
    buffs.append((before, after))
buffs.reverse()
for pair in buffs:
    (table[pair[0]], table[pair[1]]) = (table[pair[1]], table[pair[0]])
ret = ''
for ch in name:
    ret += chr(table[ord(ch) - ord('a')] + ord('a'))
print(ret)
