n = int(input())
rs = [0 for i in range(n + 1)]
cs = [0 for i in range(n + 1)]
s = ""
for i in range(n**2):
    r, c = list(map(int, input().split()))
    if rs[r] == 0 and cs[c] == 0:
        rs[r] = 1
        cs[c] = 1
        s += str(i + 1) + " "
print(s)
