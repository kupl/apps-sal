i = input()
l = list(map(int, input().split()))

dl = list(sorted(l))
dl = list(reversed(dl))

ans = 0

for i in range(len(dl)):
    if i % 2 == 0:
        ans += dl[i]
    else:
        ans -= dl[i]

print(ans)
