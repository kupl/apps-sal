n = int(input())
a = list(map(int, input().split()))

if sorted(a) == list(range(1, n + 1)):
    print(0)
    print(' '.join(map(str, a)))
else:
    cnt = [0] * (n + 1)
    for i in a:
        cnt[i] += 1

    add = []
    for i in range(1, n + 1):  # 1 to 26
        if cnt[i] == 0:
            add.append(i)

    pos = 0
    m_cnt = 0
    appeared = [False] * (n + 1)
    for i, t in enumerate(a):
        if cnt[t] > 1:
            if t > add[pos] or appeared[t]:
                a[i] = add[pos]
                pos += 1
                m_cnt += 1
                if pos == len(add):
                    break
                cnt[t] -= 1
                appeared[a[i]] = True
            else:
                appeared[t] = True
        else:
            appeared[t] = True

    print(m_cnt)
    print(' '.join(map(str, a)))
