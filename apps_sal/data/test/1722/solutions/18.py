n = int(input())
sp = [0] * 26
for i in range(n):
    st = input()
    sp[ord(st[0]) - ord("a")] += 1
sm = 0
for x in sp:
    ch = x // 2
    sm += ch * (ch - 1) // 2
    sm += (x - ch) * (x - ch - 1) // 2
print(sm)
