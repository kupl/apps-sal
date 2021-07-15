n = int(input())
hand = []
deck = []
s = [-1] * (n + 1)
for el in map(int, input().split()):
    hand.append(el)
    s[el] = 0
i = 1
for el in map(int, input().split()):
    deck.append(el)
    s[el] = i
    i += 1
if s[1] != 0:
    i = 2
    while i <= n and s[i] == s[1] + i - 1:
        i += 1
    if s[i - 1] == n:
        j = i
        while j <= n and s[j] <= j - i:
            j += 1
        if j > n:
            print(n - i + 1)
            return
ans = 0
for i in range(1, n + 1):
    ans = max(ans, s[i] - i + 1 + n)
print(ans)

