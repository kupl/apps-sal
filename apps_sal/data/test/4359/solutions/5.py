from operator import itemgetter
l = [int(input()) for _ in range(5)]
for i in range(5):
    l[i] += 9
    l[i] = str(l[i])
l.sort(key=itemgetter(-1), reverse=True)
for i in range(5):
    l[i] = int(l[i])
    l[i] -= 9
ans = 0
for i in range(5):
    if l[i] % 10 == 0:
        ans += l[i]
    else:
        if i == 4:
            ans += l[i]
        else:
            ans += l[i] + 10 - l[i] % 10
print(ans)
