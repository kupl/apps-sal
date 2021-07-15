n, k = list(map(int, input().split()))
r, s, p = list(map(int, input().split()))
t = list(input())

scr = 0
#k回目までの処理
for i in range(k):
    if t[i] == "r":
        scr += p
    elif t[i] == "s":
        scr += r
    elif t[i] == "p":
        scr += s
#print(scr)

#k＋１回目以降の処理
#前に出した手のせいで勝てない場合は、次の手の邪魔にならないような手を出す
for i in range(k, n):
    if t[i] == t[i - k]:
        scr += 0
        t[i] = "q"
    else:
        if t[i] == "r":
            scr += p
        elif t[i] == "s":
            scr += r
        elif t[i] == "p":
            scr += s

print(scr)

