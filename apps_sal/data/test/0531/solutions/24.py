n = int(input())
x = list(map(int, input().split()))

ln = len(set(x))

if ln <= 2 and max(x) - min(x) <= 1:
    print(n)
    print(' '.join(map(str, x)))

else:
    abc = sorted(set(x))

    if len(abc) == 2:
        abc.insert(1, (abc[0] + abc[1]) // 2)

    co = [x.count(el) for el in abc]

    ans = n
    a, b, c = co
    ans_co = [a, b, c]

    while b >= 2:
        b -= 2
        a += 1
        c += 1

        s = min(a, co[0]) + min(b, co[1]) + min(c, co[2])
        if s < ans:
            ans = s
            ans_co = [a, b, c]

    a, b, c = co

    while min(a, c) > 0:
        a -= 1
        c -= 1
        b += 2

        s = min(a, co[0]) + min(b, co[1]) + min(c, co[2])
        if s < ans:
            ans = s
            ans_co = [a, b, c]

    print(ans)
    print(' '.join([' '.join([str(abc[j]) for i in range(ans_co[j])]) for j in range(3)]).strip())

