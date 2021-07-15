from collections import deque
N = int(input())
S = deque([3, 5, 7])
ans = 0
for _ in range(3**10):
    a = S.popleft()
    if a <= N:
        tmp = a
        j3, j5, j7 = False, False, False
        while tmp > 0:
            if tmp%10 == 3:
                j3 = True
            elif tmp%10 == 5:
                j5 = True
            else:
                j7 = True
            tmp //= 10
        if j3 and j5 and j7:
            ans += 1
    S.append(a*10+3)
    S.append(a*10+5)
    S.append(a*10+7)
print(ans)


