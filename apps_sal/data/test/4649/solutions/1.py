def givestringsk(k):
    t = ["R", "G", "B"]
    ans = []
    for i in range(3):
        temp = ""
        for j in range(i, i + k):
            temp += t[j % 3]
        ans.append(temp)
    return ans


def countdifferences(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    s = input()
    temp = givestringsk(k)
    ans = 10000000000000
    for i in range(k, n + 1):
        for j in range(3):
            ans = min(ans, countdifferences(s[i - k:i], temp[j]))
    print(ans)
