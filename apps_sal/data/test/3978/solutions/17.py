n = int(input())
a = list(sorted(map(int, input().split())))
ans = 0
divs = []
for x in a:
    if all((x % d != 0 for d in divs)):
        ans += 1
        divs.append(x)
print(ans)
