n = int(input())
for i in range(n):
    x = input()
    hasz, hasd, ans = 0, 0, 0
    for b in x:
        a = int(b)
        if a == 0:
            hasz += 1
        if a % 2 == 0:
            hasd += 1
        ans += a
    if hasz:
        hasd -= 1
    if hasz and hasd and ans % 3 == 0:
        print('red')
    else:
        print('cyan')
