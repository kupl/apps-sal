n = int(input())
alphabet_cnt = [[0] * n for i in range(26)]
alphabet = list('abcdefghijklmnopqrstuvwxyz')
alphabet_map = dict(zip(alphabet, list(range(26))))
for i in range(n):
    si = input()
    for j in range(len(si)):
        alphabet_cnt[alphabet_map[si[j]]][i] += 1
alphabet_intersect = [min(alp) for alp in alphabet_cnt]
print(''.join([alphabet[idx] * cnt for (idx, cnt) in enumerate(alphabet_intersect)]))
