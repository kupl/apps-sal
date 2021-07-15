q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    s = input()
    ans = k
    sample = "RGB"
    for i in range(n - k + 1):
        cnt = 0
        x = 0
        for j in range(i, i + k):
            if s[j] != sample[x]:
                cnt += 1
            x = (x + 1) % 3
        #print(ans, 7)
        ans = min(ans, cnt)
        cnt = 0
        x = 1
        for j in range(i, i + k):
            if s[j] != sample[x]:
                cnt += 1
            x = (x + 1) % 3
        ans = min(ans, cnt)
        #print(ans, 8)
        cnt = 0
        x = 2
        for j in range(i, i + k):
            if s[j] != sample[x]:
                cnt += 1
            x = (x + 1) % 3
        ans = min(ans, cnt) 
        #print(ans, 9)       
    print(ans)
