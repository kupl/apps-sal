n = int(input(''))
s = list(map(int, input().split()))
cnt = 0
s.sort()
for i in range(0, n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if s[i] != s[j] != s[k]:
                if s[i] + s[j] > s[k]:
                    cnt += 1
print(cnt)
