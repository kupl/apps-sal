for _ in range(int(input())):
    a, b, c, n = map(int, input().split())
    s = a + b + c
    mx = max(a, b, c)
    if((s + n) % 3 == 0 and (s + n) // 3 >= mx):
        print("YES")
    else:
        print("NO")
