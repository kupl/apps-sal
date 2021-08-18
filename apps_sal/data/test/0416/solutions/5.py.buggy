n, m = list(map(int, input().split()))
s = input()
cnt = int(0)
for ch in s:
    if ch == 'N':
        cnt += 1
    elif cnt > m:
        print("NO")
        return
    else:
        cnt = int(0)
if cnt > m:
    print("NO")
    return
s = "Y" + s
for i in range(0, n + 1):
    if s[i] == '?' or s[i] == 'Y':
        cnt = int(0)
        for j in range(i + 1, n + 1):
            #print(i, j, cnt, end = "\n")
            if s[j] == 'Y':
                if cnt == m:
                    print("YES")
                    return
                break
            if s[j] == '?':
                if cnt == m:
                    print("YES")
                    return
            cnt += 1
        if cnt == m:
            print("YES")
            return
print("NO")
