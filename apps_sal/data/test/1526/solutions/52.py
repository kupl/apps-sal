abc = sorted(list(map(int, input().split())))

ans = 0
while len(set(abc)) != 1:
    ans += 1
    if abc[-1] - abc[0] >= 2:
        abc[0] += 2
    else:
        abc[0] += 1
        abc[1] += 1

    abc.sort()

print(ans)

