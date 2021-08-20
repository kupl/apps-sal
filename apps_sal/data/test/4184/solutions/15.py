n = int(input())
w = list(map(int, input().split()))
df_list = []
for t in range(n - 1):
    s1 = sum(w[:t + 1])
    s2 = sum(w[t + 1:])
    df_list.append(abs(s1 - s2))
    answer = min(df_list)
print(answer)
