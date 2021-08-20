(n, a, b) = list(map(int, input().split()))
s = input()
just_placed = None
ans = 0
for i in s:
    more_a = a > b
    if i == '.':
        if just_placed == 'a':
            if b > 0:
                b -= 1
                ans += 1
                just_placed = 'b'
            else:
                just_placed = None
        elif just_placed == 'b':
            if a > 0:
                a -= 1
                ans += 1
                just_placed = 'a'
            else:
                just_placed = None
        elif more_a:
            a -= 1
            ans += 1
            just_placed = 'a'
        elif b > 0:
            b -= 1
            ans += 1
            just_placed = 'b'
        else:
            just_placed = None
    else:
        just_placed = None
print(ans)
