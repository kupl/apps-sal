r = lambda: map(int, input().split())

a1, b1 = r()
a2, b2 = r()
a3, b3 = r()

ans = "NO"
for (a1, b1) in [(a1, b1), (b1, a1)]:
    for (a2, b2) in [(a2, b2), (b2, a2)]:
        for (a3, b3) in [(a3, b3), (b3, a3)]:
            if a1 >= a2 + a3 and b1 >= max(b2, b3):
                ans = "YES"

print(ans)
