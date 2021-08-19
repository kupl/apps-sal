t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    a = []
    s = input()
    for j in range(len(s)):
        a.append(s[j:j + 1])
    answer = (k - 1) * '()' + (n // 2 - k + 1) * '(' + (n // 2 - k + 1) * ')'
    b = []
    for j in range(len(answer)):
        b.append(answer[j:j + 1])
    ans = []
    j = 0
    while j < len(answer):
        if b[j] == a[j]:
            j += 1
        else:
            x = j + 1
            while a[x] == a[j]:
                x += 1
            ans.append([j + 1, x + 1])
            for f in range(j, j + (x - j + 1) // 2):
                (a[f], a[x - f + j]) = (a[x - f + j], a[f])
            j += 1
    print(len(ans))
    for j in range(len(ans)):
        print(' '.join(map(str, ans[j])))
