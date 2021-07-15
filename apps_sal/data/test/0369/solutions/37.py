N, M = list(map(int, input().split()))
S = input()
prev = N
pos = N
ans = []
while pos > 0:
    for i in range(M, 0, -1):
        if pos - i >= 0 and S[pos - i] == '0':
            ans.append(i)
            pos -= i
            break
    if pos == prev:
        ans = [-1]
        break
    prev = pos
print((*ans[::-1]))

