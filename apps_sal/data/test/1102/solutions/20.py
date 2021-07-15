n, a = list(map(int, input().split()))
a -= 1
t = list(map(int, input().split()))
ans = 0
R = list(range(0, n))
for dis in range(0, 100):
    l = a - dis
    r = a + dis
    if l not in R and r not in R:
        break
    elif l in R and r not in R:
        ans += t[l]
    elif l not in R and r in R:
        ans += t[r]
    elif t[l] == 1 and t[r] == 1:
        ans += 2 if l != r else 1
print(ans)

