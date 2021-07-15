n, m = map(int, input().split())
S = list(input())
"""
9 3
0001000100
0010001000
3  2   3 1  
"""
S_r = S[::-1] + ["0"] #スタートのぶん付け足し
ans = []
now = 0
while now < n:
    flg = True
    for i in range(m,0,-1):
        if now + i <= n and S_r[now+i] == "0":
            ans.append(i)
            now += i
            flg = False
            break
    if flg:
        print(-1)
        return

print(*ans[::-1])
