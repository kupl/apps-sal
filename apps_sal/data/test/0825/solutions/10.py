def factrize(num):
    factor = {}
    div = 2
    s = int(num**0.5)+1
    while div < s:
        div_cnt = 0
        while num % div == 0:
            div_cnt += 1
            num //= div
        if div_cnt != 0:
            factor[div] = div_cnt
        div += 1
    if num > 1:
        factor[num] = 1
    return factor
  
n = int(input())
cnt = factrize(n)

ans = 0
for c in cnt.values():
    tmp = 1
    while c >= tmp:
        c -= tmp
        ans += 1
        tmp += 1      
print(ans)
