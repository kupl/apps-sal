ABC = list(map(int, input().split()))
odds = [x for x in ABC if x % 2]
evens = [x for x in ABC if x % 2 == 0]

ans = 0
if len(odds) == 2:
    odds[0] += 1
    odds[1] += 1
    ans += 1
elif len(evens) == 2:
    evens[0] += 1
    evens[1] += 1
    ans += 1
ABC = sorted(odds + evens)
ans += (ABC[2] - ABC[0]) // 2 + (ABC[2] - ABC[1]) // 2
print(ans)

