n = int(input())
a = list(map(int, input().split()))
s = list([True if x == "1" else False for x in list(input())])
i = 0
while i < n:
    if i == n - 1:
        if a[-1] != n:
            print("NO")
    elif not s[i]:
        if a[i] - 1 != i:
            print("NO")
            return
    else:
        start = i
        i += 1
        while(i < len(s) and s[i]):
            i += 1
        end = i
        test = a[start: end + 1]
        #print([start, end, test])
        if not (max(test) == end + 1 and min(test) == start + 1):
            print("NO")
            return

    i += 1
print("YES")
