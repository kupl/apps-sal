n = int(input())
a = list(map(int, input().split()))
if 0 in a:
    if len(set(a)) > 1:
        print('Impossible')
    else:
        print('Possible')
        print(*[1] * n)
elif not all((q < n for q in a)):
    print('Impossible')
else:
    s = {}
    answer = [0 for q in range(n)]
    for q in range(len(a)):
        if a[q] in s:
            s[a[q]].append(q)
        else:
            s[a[q]] = [q]
    q2 = 0
    for q in s:
        if len(s[q]) % (n - q) != 0:
            print('Impossible')
            break
        for q1 in range(len(s[q])):
            if q1 % (n - q) == 0:
                q2 += 1
            answer[s[q][q1]] = q2
    else:
        print('Possible')
        print(*answer)
