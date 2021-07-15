n = int(input())
p = list(map(int, input().split()))

good = True
for i in range(n):
    s = input()
    q = 0
    for l in s:
        if l in "aeiouy":
            q += 1
    if q != p[i]:
        good = False

print("YES" if good else "NO")
