N = int(input())

hatsugen = [[] for _ in range(N)]
# print(hatsugen)
A = -1
while True:
    try:
        s = input()
    except EOFError:
        break
    a = tuple(map(int, s.rstrip().split()))
    # print(a)
    if len(a) == 1:
        A += 1
    else:
        hatsugen[A].append(a)
# print(hatsugen)

ans = 0
for i in range(2**N):

    bit = i
    flag = [0] * N
    idx = 0
    while bit:
        if (bit & 1):
            flag[idx] = 1
        bit >>= 1
        idx += 1

    flag2 = 0
    # print(flag)
    for i in range(N):
        if flag[i]:
            hatsu = hatsugen[i]
        else:
            continue
        for word in hatsu:
            # print(*word)
            if flag[word[0] - 1] != word[1]:
                flag2 = 1
                # print("false")
                break
        if flag2:
            break
    if flag2 == 0:
        ans = max(ans, sum(flag))

print(ans)
