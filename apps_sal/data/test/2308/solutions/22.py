def mp():
    return map(int, input().split())


t = int(input())
for tt in range(t):
    x = input()
    y = input()
    x = x[::-1]
    y = y[::-1]
    x_i = x.find('1')
    y_i = y.find('1')
    if x_i >= y_i:
        print(x_i - y_i)
    else:
        for i in range(y_i, len(x)):
            if x[i] == '1':
                print(i - y_i)
                break
