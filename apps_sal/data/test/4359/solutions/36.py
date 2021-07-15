data = [int(input()) for i in range(5)]
if all(i % 10 == 0 for i in data):
    print((sum(data)))
else:
    a = 10
    for i in range(len(data)):
        if data[i] % 10 != 0:
            if a > data[i] % 10:
                a = data[i] % 10
                b = i
    ans = 0
    for i in range(len(data)):
        if i != b:
            if data[i] % 10 != 0:
                ans += (data[i] // 10 + 1) * 10
            else:
                ans += data[i]
        else:
            ans += data[i]
    print(ans)

