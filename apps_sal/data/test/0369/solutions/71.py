(N, M) = map(int, input().split())
S = input()
pos = N
ans = []
while pos > 0:
    for i in range(M, 0, -1):
        if pos - i < 0 or S[pos - i] == '1':
            continue
        ans.append(i)
        pos -= i
        break
    else:
        ans = [-1]
        break
print(*ans[::-1])
