N = int(input())
S = input()

ans = 0
buf = ""
for l in S:
    if buf != l:
        buf = l
        ans += 1
    else:
        pass
print(ans)
