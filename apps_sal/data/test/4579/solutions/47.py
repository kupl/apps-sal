n = int(input())
s = [input() for _ in range(n)]  # リスト内包表記

ss = set(s)
ans = len(ss)
print(ans)
