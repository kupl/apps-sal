n, k = list(map(int, input().split()))
d = set(map(int, input().split()))

while True:
    tmp_str = set(str(n))
    for i in tmp_str:
        if int(i) in d:
            n += 1
            break
    else:
        print(n)
        break
