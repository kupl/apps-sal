s = input()
m = int(input())
for i in range(m):
    l, r, k = map(int, input().split())
    l = l - 1
    r = r - 1
    sub = s[l: r + 1]
    k = k % len(sub)
    part1 = sub[0: len(sub) - k]
    part2 = sub[len(sub) - k: len(sub)]
    sub = part2 + part1
    s = list(s)
    s[l: r + 1] = sub[0: len(sub)]
    s = "".join(s)
print(s)
