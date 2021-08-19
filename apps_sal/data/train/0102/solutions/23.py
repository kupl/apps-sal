g = int(input())
for i in range(g):
    a = int(input())
    ans = 0
    if a >= 10:
        ans += 9
    else:
        ans += a
        print(ans)
        continue
    for i in range(2, 11):
        if 10 ** i <= a:
            ans += 9
        else:
            for j in range(1, 10):
                if int(str(j) * i) <= a:
                    ans += 1
                else:
                    break
            break
    print(ans)
