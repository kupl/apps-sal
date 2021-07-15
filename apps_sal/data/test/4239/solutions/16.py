def sub_cnt(c, b):
    cnt = 0
    for i in b:
        while c >= i:
            c -= i
            cnt += 1
    return cnt

n = int(input())

b6 = [6**i for i in range(6, -1, -1)]
b9 = [9**i for i in range(5, -1, -1)]

ans = 10**9
n9 = n // 9
for c9 in range(n9+1):
    cnt = 0
    cn = n - c9*9
    c6 = cn // 6
    c1 = cn % 6
    
    cnt += sub_cnt(c9, b9)
    cnt += sub_cnt(c6, b6)
    cnt += c1
    ans = min(ans, cnt)
print(ans)
