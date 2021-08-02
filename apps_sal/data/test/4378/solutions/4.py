n = int(input())
s = input()
s = [i for i in s]
ans = 0
e = ["R", "G", "B"]
for i in range(1, n):
    if s[i] == s[i - 1]:
        ans += 1
        dame = set()
        dame.add(e.index(s[i - 1]))
        if i != n - 1:
            dame.add(e.index(s[i + 1]))
        for j in range(3):
            if j in dame:
                continue
            else:
                s[i] = e[j]
                break
print(ans)
print("".join(s))
