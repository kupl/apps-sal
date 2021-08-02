import string
n = int(input())
a = []
for i in range(n):
    a.append(input())
ans = 0
small = string.ascii_lowercase
for i in small:
    for j in small:
        tmp = 0
        for s in a:
            cnt = 0
            for c in s:
                if c == i or c == j:
                    cnt += 1
            if cnt == len(s):
                tmp += len(s)
        ans = max(ans, tmp)
print(ans)
