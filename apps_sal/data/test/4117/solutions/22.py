n = int(input())
l = list(map(int, input().split()))
cnt = 0
for a in range(n - 2):
    for b in range(a + 1, n - 1):
        for c in range(b + 1, n):
            if len(set([l[a], l[b], l[c]])) == 3:
                if l[a] + l[b] > l[c] and l[b] + l[c] > l[a] and l[c] + l[a] > l[b]:
                    cnt += 1
print(cnt)
