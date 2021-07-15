n = input()

mx = 9 ** int((len(n) - 1))
if len(n) == 1:
    print(n)
    return
cnt = 1
for i in n:
    cnt *= int(i)
if cnt > mx:
    mx = cnt
for i in range(len(n)):
    cur = n

    if cur[i] != "0":
        cur = cur[:i] + str(int(cur[i]) - 1) + "9" * (len(n) - i - 1)
    cnt = 1


    for j in cur:
        cnt *= int(j)
    if cnt > mx:
        mx = cnt

print(mx)

