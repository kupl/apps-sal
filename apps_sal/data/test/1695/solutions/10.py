def increase(cnt, letter):
    if letter not in cnt:
        cnt[letter] = 1
    else:
        cnt[letter] += 1


n, m = list(map(int, input().split()))

strings = []

for i in range(n):
    strings.append(input())

points = list(map(int, input().split()))

ans = 0

for qu in range(m):
    cnt = {}
    mx = 0
    for person in range(n):
        increase(cnt, strings[person][qu])
        mx = max(mx, cnt[strings[person][qu]])
    ans += points[qu] * mx

print(ans)
