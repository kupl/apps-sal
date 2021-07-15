
N, M = list(map(int, input().split()))
s = input()
ans = []
cur = N
while cur != 0:
    for step in range(M, 0, -1):
        if cur - step < 0:
            continue
        if s[cur-step] == '1':
            continue
        ans.append(step)
        cur -= step
        break
    else:
        print((-1))
        return
print((*ans[::-1]))

