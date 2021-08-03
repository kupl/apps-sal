N, s, l = int(input()), [ord(x) - ord('a') for x in input()], [int(x) for x in input().split()]
arr = [[1, l[s[0]]]]
total = 1
ma = 1
t = 1
mi = 1
for c in s[1:]:
    tmp = 0
    for i in range(len(arr)):
        arr[i][1] = min(arr[i][1], l[c])
        if i + 1 >= arr[i][1]:
            arr = arr[:i]
            if(t > i):
                t = 0
                mi += 1
            break
        else:
            tmp += arr[i][0]
    t += 1
    arr.insert(0, [total, l[c]])
    ma = max(ma, len(arr))
    total += tmp
    total %= 10 ** 9 + 7
print(total)
print(ma)
print(mi)
