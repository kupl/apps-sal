n, m = map(int, input().split())
p = []
s = []
for i in range(m):
    P, S = input().split()
    p.append(int(P))
    s.append(S)
question = [0] * n  # それぞれの問題のWAの数
ac = 0
wa = 0
for i in range(m):
    if question[p[i] - 1] != -1:
        if s[i] == "AC":
            ac += 1
            wa += question[p[i] - 1]
            question[p[i] - 1] = -1
        else:
            question[p[i] - 1] += 1
print(str(ac) + " " + str(wa))
