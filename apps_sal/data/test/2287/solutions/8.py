N = int(input())
for _ in range(N):
    s = input()
    first = -1
    last = -1
    for i in range(len(s)):
        if s[i] == '1':
            if first == -1:
                first = i
            last = i
    cnt = 0
    if first == -1:
        print(0)
        continue
    for i in range(first, last + 1):
        if s[i] == '0':
            cnt += 1
    print(cnt)
