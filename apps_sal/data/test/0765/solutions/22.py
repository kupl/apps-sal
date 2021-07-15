t, s, q = map(int, input().split())
i = 0
while(s < t):
    s *= q; i += 1
print(i)
