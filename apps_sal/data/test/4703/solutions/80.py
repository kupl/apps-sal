ss = input()
l = len(ss) - 1
ans = 0
for i in range(2**l):
    s = ss
    for j in reversed(range(l)):
        if i & (2**j) > 0:
            s = s[:j + 1] + " " + s[j + 1:]
    num = list(map(int, s.split(" ")))
    ans += sum(num)
print(ans)
