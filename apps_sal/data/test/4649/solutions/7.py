def user99():
    text = 'RGB' * 2222
    for _ in range(int(input())):
        n, k = list(map(int, input().split()))
        s = input()
        ans = 2222
        for i in range(3):
            p = text[i: k + i]
            #print("p = ", p)
            for j in range(n - k + 1):
                diff = 0
                #print(s[j: j + k], "vs", p)
                for l in range(j, j + k):
                    if s[l] != p[l - j]:
                        diff += 1
                ans = min(ans, diff)
        print(ans)

user99()

