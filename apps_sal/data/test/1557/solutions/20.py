h1, a1, c1 = list(map(int, input().split()))
h2, a2 = list(map(int, input().split()))

ans = list()
while True:
    if h1 <= a2 and h2 > a1:
        ans.append('HEAL')
        h1 += c1
    else:
        ans.append('STRIKE')
        h2 -= a1
        if h2 <= 0:
            break

    h1 -= a2

print(len(ans))
print('\n'.join(ans))
