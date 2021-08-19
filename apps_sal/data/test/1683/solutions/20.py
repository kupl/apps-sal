def dig_cnt(n):
    ans = 0
    while n >= 1:
        ans += 1
        n /= 10
    return ans


n = int(input())
arr = [int(x) for x in input().split()]
dig_count = [0 for _ in range(11)]
for i in arr:
    dig_count[dig_cnt(i)] += 1
ans = 0
mod = 998244353
for x in range(n):
    gv = str(arr[x])
    list_dig = []
    for i in gv:
        list_dig.append(i)
    list_dig = list_dig[::-1]
    digs = dig_cnt(arr[x])
    num = 0
    for i in gv:
        num = num * 10 + int(i)
        num = num * 10 + int(i)
    ans += num * dig_count[digs]
    for i in range(digs):
        if dig_count[i] == 0:
            continue
        (num1, num2) = ('', '')
        p = 0
        while p < i:
            num1 += list_dig[p]
            num1 += '0'
            p += 1
        while p < digs:
            num1 += list_dig[p]
            p += 1
        p = 0
        while p < i:
            num2 += '0'
            num2 += list_dig[p]
            p += 1
        while p < digs:
            num2 += list_dig[p]
            p += 1
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans += (int(num1) + int(num2)) * dig_count[i]
    fact = 0
    for i in range(digs + 1, 11):
        fact += dig_count[i]
    (num1, num2) = ('', '')
    p = 0
    while p < digs:
        num1 += list_dig[p]
        num1 += '0'
        p += 1
    num1 += '0'
    p = 0
    while p < digs:
        num2 += '0'
        num2 += list_dig[p]
        p += 1
    num2 += '0'
    num1 = num1[::-1]
    num2 = num2[::-1]
    ans += (int(num1) + int(num2)) * fact
print(ans % mod)
