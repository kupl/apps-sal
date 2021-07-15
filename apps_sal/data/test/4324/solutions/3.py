t = int(input())
alph = "abcdefghijklmnopqrstuvwxyz"
for _ in range(t):
    n, a, b = map(int, input().split())
    ans = [alph[i] for i in range(b)]
    while len(ans) < n:
        ans.append(ans[len(ans) - b])
    print("".join(ans))
