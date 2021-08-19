q = int(input())
for query in range(q):
    s = input()
    t = input()
    p = input()
    pointer_s = 0
    pointer_t = 0
    no = 0
    miejsca = []
    while pointer_s < len(s):
        while True:
            if pointer_t >= len(t):
                no = 1
                break
            elif t[pointer_t] != s[pointer_s]:
                pointer_t += 1
            else:
                pointer_s += 1
                miejsca.append(pointer_t)
                pointer_t += 1
                break
        if no == 1:
            break
    if no == 0:
        literki = [0] * 400
        for i in range(len(t)):
            if i not in miejsca:
                literki[ord(t[i])] += 1
        for i in range(len(p)):
            literki[ord(p[i])] -= 1
        for i in range(400):
            if literki[i] > 0:
                no = 1
                break
    if no == 0:
        print('YES')
    else:
        print('NO')
