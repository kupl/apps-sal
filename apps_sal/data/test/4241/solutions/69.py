S = input()
T = input()


ans = 100000  # 適当に1001以上にを初期値にしておきます

# Tが1文字のときlen(S)回、2文字のときlen(s) -1回....なので,
# les(S)-len(T)+1回です
for i in range(len(S) - len(T) + 1):
    score = 0
    U = S[i:i + len(T)]  # Sのi文字目から連続するlen(T)文字を,Uとします
    for j in range(len(T)):
        if U[j] != T[j]:
            score += 1
    ans = min(ans, score)

print(ans)

