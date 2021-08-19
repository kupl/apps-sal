k = int(input())
s = input()
n = len(s)
li = [0]
# print("ASD")
for i in range(n):
    if s[i] == "-" or s[i] == " ":
        li.append(i)
li.append(n - 1)
if len(li) == 0:
    print(n)
else:
    # print(len(s))
    # print(li)
    def func(m):
        i, j, count = m - 1, 0, 0
        while(i <= n - 1):
            p = j
            while(p < len(li)):
                if li[p] > i:
                    break
                p += 1
            if p - j == 1:
                return False
            i = li[p - 1] + m
            # print(li[p-1])
            j = p - 1
            count += 1
            if count > k:
                # print(count)
                return False
        # print(i)
        if i - m < n - 1:
            count += 1
        # print(count)
        return count <= k
    # print(func(4))
    low = li[1] + 1
    # print(low)

    high = n
    ans = 0
    while(low <= high):
        mid = (low + high) // 2
        check = func(mid)
        if check:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)
