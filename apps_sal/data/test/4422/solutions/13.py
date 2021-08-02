N, K = map(int, input().split())
moji = str(input())
ans = moji[:K - 1] + moji[K - 1].lower() + moji[K:]
print(ans)
