T = int(input())

for t in range(T):
    N = int(input())
    s = input()

    if '<' not in s or '>' not in s:
        print(N)
    else:
        cnt = 0
        for i in range(N):
            prev = i - 1
            if prev < 0:
                prev += N
            if s[i] == '-' or s[prev] == '-':
                cnt += 1
        print(cnt)
