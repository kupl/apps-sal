n, m = list(map(int, input().split()))
k = set()
s = ""
ans = ""
for i in range(n):
    new_s = input()
    if new_s[::-1] in k:
        ans += new_s
    elif new_s == new_s[::-1]:
        s = new_s
    k.add(new_s)
print(2 * len(ans) + len(s))
print(ans + s + ans[::-1])
