B = [0] * (10 ** 5 + 2)
S = [0] * (10 ** 5 + 2)
a, b = list(map(int, input().split()))
for i in range(a):
    l = list(map(str, input().split()))
    if l[0] == 'S':
        S[int(l[1])] += int(l[2])
    if l[0] == 'B':
        B[int(l[1])] += int(l[2])
count = 0
ans = []
for i in range(10 ** 5 + 2):
    if S[i] != 0:
        count += 1
        ans.append(('S', i, S[i]))
        if count == b:
            break
for i in range(len(ans) - 1, -1, -1):
    print(ans[i][0], ans[i][1], ans[i][2])
count = 0
for i in range(10 ** 5 + 1, -1, -1):
    if B[i] != 0:
        count += 1
        print('B', i, B[i])
        if count == b:
            break
