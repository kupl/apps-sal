n = int(input())
s = input()

ans = 0

for i in range(n):
    # 複数のリストから共通する要素を抽出
    ans = max(ans, len(set(list(s[:i])) & set(list(s[i:]))))

print(ans)
