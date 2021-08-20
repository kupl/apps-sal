N = int(input())
K = int(input())
x = list(map(int, input().split()))
ans = 0
for i in x:
    if i <= K - i:
        ans += i
    if i > K - i:
        ans += K - i
print(2 * ans)
