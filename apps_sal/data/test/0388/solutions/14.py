def solve(n, k, a):
    t = 0
    ans = ['' for i in range(n)]
    i = 0
    while i < len(a) and a[i] == 'NO':
        ans[i] = names[0]
        i += 1
    if i == len(a):
        for j in range(i, i + k - 1):
            ans[j] = ans[0]
        return ans
    for j in range(i, i + k):
        ans[j] = names[t]
        t += 1
    while i < len(a):
        if a[i] == 'NO':
            ans[i + k - 1] = ans[i]
        else:
            ans[i + k - 1] = names[t]
            t += 1
        i += 1
    return ans


names = []
for i in range(ord('A'), ord('Z') + 1):
    for j in range(ord('a'), ord('z') + 1):
        names.append(chr(i) + chr(j))
"\nimport random\nfor i in range(100000):\n    n = random.randint(2, 52)\n    k = random.randint(2, n)\n    a = [random.choice(['YES', 'NO']) for i in range(n - k)]\n    ans = solve(n, k, a)\n    for i in range(0, n - k):\n        s = set(ans[i:i+k])\n        is_diff = len(s) == k\n        if (a[i] == 'YES'):\n            if (len(s) != k):\n                print(n, k)\n                print(a)\n                print(ans)\n                exit\n        if (a[i] == 'NO'):\n            if (len(s) == k):\n                print(n, k)\n                print(a)\n                print(ans)\n                exit\n"
(n, k) = list(map(int, input().strip().split()))
is_ok = input().strip().split()
ans = solve(n, k, is_ok)
print(*ans)
