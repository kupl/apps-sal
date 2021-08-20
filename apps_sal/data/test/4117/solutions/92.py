n = int(input())
lll = list(map(int, input().split()))
lll.sort()
len_lll = len(lll)
ans = 0
for i in range(len_lll):
    a = lll[i]
    for j in range(i + 1, len_lll):
        b = lll[j]
        for k in range(j + 1, len_lll):
            c = lll[k]
            if a + b > c and a != b and (b != c):
                ans += 1
print(ans)
