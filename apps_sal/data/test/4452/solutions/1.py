t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    ans = []
    for i in range(n):
        if s[i] != "0":
            ans.append(s[i] + "0" * (n - 1 - i))
    print(len(ans))
    print(*ans)
