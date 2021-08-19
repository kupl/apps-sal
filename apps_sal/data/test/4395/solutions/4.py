from itertools import permutations

n = int(input())
seq = input()

ls = list(permutations("RGB"))
for i in range(len(ls)):
    ls[i] = ''.join(ls[i])

strans = ""
ans = n
for tes in ls:
    tes = (tes * (n // 3 + 1))
    cur = 0
    for i in range(len(seq)):
        if tes[i] != seq[i]:
            cur += 1
    if cur < ans:
        ans = min(ans, cur)
        strans = tes[:len(seq)]
    # print(tes, seq, ans, cur)
print(ans)
print(strans)
