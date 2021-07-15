N = int(input())
S, T = list(input().split())

new_str = []

# SとTのリストを互いに足したやつを新しいリストに入れる
for i in range(0, N):
    new_str.append(S[i] + T[i])

# リスト内をくっつけて出力
print((''.join(new_str)))

