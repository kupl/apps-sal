s, p = map(int,input().split())
ans = False
i = 1
while (i * i <= p):
    if i * (s - i) == p:
        ans = True
    i += 1
print("Yes" if ans else "No")
