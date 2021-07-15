def resolve():
    s = input()
    t = input()
    cnt = 0
    for i,j in zip(s,t):
        if i==j: cnt += 1
    print(cnt)
resolve()
