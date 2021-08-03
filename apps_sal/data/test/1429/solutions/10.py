# 問題文の意味はまったくわからんが、とりあえず部分列でAとTの数およびCとGの数が同じところの数、ってこと？
line = input().split()
n, s = int(line[0]), list(line[1])
ans = 0
for i in range(n - 1):
    d = {"A": 0, "T": 0, "C": 0, "G": 0}
    d[s[i]] += 1
    for j in range(i + 1, n):
        d[s[j]] += 1
        if d["A"] == d["T"] and d["C"] == d["G"]:
            ans += 1
print(ans)
