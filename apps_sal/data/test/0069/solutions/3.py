for _ in range(int(input())):
    (n, x) = map(int, input().split())
    s = input()
    pref = [0]
    for i in range(n):
        pref.append(pref[-1] + 2 * (s[i] == '0') - 1)
    jump = pref.pop()
    if jump == 0:
        print(-1 * (min(pref) <= x <= max(pref)))
    else:
        tot = 0
        for delta in pref:
            if (x - delta) % jump == 0 and (x - delta) // jump >= 0:
                tot += 1
        print(tot)
