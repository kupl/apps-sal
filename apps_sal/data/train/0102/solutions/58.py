t = int(input())
for _ in range(t):
    s = input()
    g = len(s)
    cnt = 9 * (g - 1)
    let = 1
    j = int(str(let) * g)
    while j <= int(s):
        cnt += 1
        let += 1
        j = int(str(let) * g)
    print(cnt)
