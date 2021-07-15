t = int(input())
while t:
    s = input()
    arr = []
    k = 0
    for i in s:
        if i == '1':
            k += 1
        else:
            arr.append(k)
            k = 0
    if k:
        arr.append(k)
    arr.sort(reverse=True)
    ans = 0
    for i in range(0, len(arr), 2):
        ans += arr[i]
    print(ans)
    t -= 1

