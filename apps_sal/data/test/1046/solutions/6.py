input()
d = input().split()
ans = 0
for i in d:
    if d.count(i) > 2 and i != '0':
        print(-1)
        break
    elif d.count(i) == 2 and i != '0':
        ans += 1
else:
    print(ans // 2)
