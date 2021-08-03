N = int(input())
m = dict()

prev = input()
m[prev] = True
flg = True

for _ in range(N - 1):
    s = input()
    flg = all([flg, s not in m, prev[len(prev) - 1] == s[0]])
    m[s] = True
    prev = s

print("Yes" if flg else "No")
