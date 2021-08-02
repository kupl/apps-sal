import bisect


q = int(input())
for _ in range(q):
    n, k = list(map(int, input().split()))
    s = input()
    ans = []
    for i in range(n):
        if s[i] == "0":
            ans.append(i)
    cnt = 0
    for i, pos in enumerate(ans):
        if cnt + pos - i <= k:
            cnt += (pos - i)
        else:
            res = list("0" * i + "1" * (pos - i) + s[pos:])
            res[pos] = "1"
            res[pos - (k - cnt)] = "0"
            print("".join(res))
            break
    else:
        print("0" * len(ans) + "1" * (n - len(ans)))
