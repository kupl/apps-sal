sd = input()
t = input()

n = len(sd)
m = len(t)
s = []

# sd を後ろから見ていき、 t の入りそうな場所を探す
for i in range(n - m, -1, -1):
    t_kamo = sd[i:i + m]
    for j in range(m + 1):
        # 1文字ずつ順に入りうるか調べ、最後まで入るなら "?" を "a" に置き換えて出力
        if j == m:
            print((sd[:i] + t + sd[i + len(t):]).replace("?", "a"))
            return
        if t_kamo[j] == "?":
            continue
        elif t_kamo[j] != t[j]:
            break

print("UNRESTORABLE")
