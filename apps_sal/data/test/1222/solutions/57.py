from collections import deque
K = int(input())

if K <= 10:
    print(K)

else:
    cnt = 9
    l = deque(list(range(1, 10)))
    while True:
        a = l.popleft()
        a1 = a % 10
        if a1 != 0:
            a2 = a * 10 + a1 - 1
            cnt += 1
            if cnt == K:
                print(a2)
                break
            l.append(a2)

        a2 = a * 10 + a1
        cnt += 1
        if cnt == K:
            print(a2)
            break
        l.append(a2)

        if a1 != 9:
            a2 = a * 10 + a1 + 1
            cnt += 1
            if cnt == K:
                print(a2)
                break
            l.append(a2)
