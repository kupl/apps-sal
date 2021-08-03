for _ in range(int(input())):
    s = input()
    t = [i for i in s.split("0") if i != ""]
    t.sort(reverse=True)
    cnt = 0
    for i in range(0, len(t), 2):
        cnt += len(t[i])
    print(cnt)
