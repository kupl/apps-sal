k = int(input())
s = input()
n = len(s)
li = [0]
for i in range(n):
    if s[i] == '-' or s[i] == ' ':
        li.append(i)
li.append(n - 1)
if len(li) == 0:
    print(n)
else:

    def func(m):
        (i, j, count) = (m - 1, 0, 0)
        while i <= n - 1:
            p = j
            while p < len(li):
                if li[p] > i:
                    break
                p += 1
            if p - j == 1:
                return False
            i = li[p - 1] + m
            j = p - 1
            count += 1
            if count > k:
                return False
        if i - m < n - 1:
            count += 1
        return count <= k
    low = li[1] + 1
    high = n
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        check = func(mid)
        if check:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)
