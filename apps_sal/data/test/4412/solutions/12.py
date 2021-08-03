import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    ls = list(map(int, input().strip().split()))
    ls = list(set(ls))
    ls.sort()
    n = len(ls)
    if n == 1:
        print(ls[0])
    elif n == 2:
        if ls[1] % ls[0] == 0:
            print(ls[1])
        else:
            print(ls[0] + ls[1])
    else:
        ans = []
        for i in range(n - 1, n - 1 - 3, -1):
            c = i
            for j in range(c - 1, -1, -1):
                if ls[c] % ls[j] != 0:
                    b = j
                    break
            else:
                ans.append(ls[c])
                continue
            for k in range(b - 1, -1, -1):
                if ls[c] % ls[k] != 0 and ls[b] % ls[k] != 0:
                    a = k
                    break
            else:
                ans.append(ls[c] + ls[b])
                continue
            ans.append(ls[c] + ls[b] + ls[a])
        print(max(ans))
