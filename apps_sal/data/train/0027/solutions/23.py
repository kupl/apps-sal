def res(e):
    ans = 0
    e1 = int(e)
    while e1 % 2 == 0:
        e1 //= 2
        ans += 1
    return 2 ** ans


for i in range(int(input())):
    n = int(input())
    s = list([x for x in list(map(int, input().split())) if x % 2 == 0])
    if len(s) == 0:
        print(0)
    else:
        temp = list([x // res(x) for x in s])
        ans = 0
        s1 = set()
        while temp != s:
            for i1 in range(len(s)):
                if temp[i1] == s[i1]:
                    continue
                elif temp[i1] not in s1:
                    s1.add(temp[i1])
                    ans += 1
                    temp[i1] *= 2
                elif temp[i1] in s1:
                    temp[i1] *= 2
        print(ans)
