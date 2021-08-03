n = int(input())
s = list(input())
t = list(input())
a = []
count = 0
for i in range(n):
    if s[i] != t[i]:
        for j in range(i + 1, n):
            if s[j] == t[i]:
                c = [str(k + 1) for k in range(j - 1, i - 1, -1)]
                count += len(c)
                a += c
                s.insert(i, s[j])
                del s[j + 1]
                break
        else:
            print(-1)
            break
else:
    print(count)
    print(' '.join(a))
