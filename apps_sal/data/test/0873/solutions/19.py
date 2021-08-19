n = int(input())
s1 = input().strip()
s2 = input().strip()
ans = 0
for i in range(n):
    (a, b) = (int(s1[i]), int(s2[i]))
    if a > b:
        (a, b) = (b, a)
    ans += min(b - a, 9 - b + a + 1)
print(ans)
