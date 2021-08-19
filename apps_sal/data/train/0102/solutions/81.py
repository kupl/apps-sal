n = int(input())
for i in range(n):
    t = int(input())
    ans = (len(str(t)) - 1) * 9
    for j in range(1, 10):
        if int(len(str(t)) * str(j)) <= t:
            ans += 1
        else:
            break
    print(ans)
