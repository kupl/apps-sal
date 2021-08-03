a, b, c, k = map(int, input().split())

if k <= a + b:
    if k >= a:
        print(a)
    else:
        print(k)
else:
    c_ans = k - a - b
    print(a - c_ans)
