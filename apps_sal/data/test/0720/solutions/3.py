s1 = s2 = 0
draws = 1
ld = 0
for _ in range(int(input())):
    (n1, n2) = map(int, input().split())
    x = min(n1, n2) - max(s1, s2)
    if x >= 0:
        if max(s1, s2) > ld:
            draws += 1
        draws += x
        ld = min(n1, n2)
    (s1, s2) = (n1, n2)
print(draws)
