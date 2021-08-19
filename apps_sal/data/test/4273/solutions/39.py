n = int(input())
march = ['M', 'A', 'R', 'C', 'H']
cnt = [0] * 5
for i in range(n):
    inp = input()
    for j in march:
        if inp[0] == j:
            cnt[march.index(j)] += 1
ans = 0
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            ans += cnt[i] * cnt[j] * cnt[k]
print(ans)
