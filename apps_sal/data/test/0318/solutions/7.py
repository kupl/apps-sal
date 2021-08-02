def inc(time):
    f = time[:2]
    m = time[2]
    s = time[3:]
    if s == '59':
        s = '00'
        if f == '23':
            f = '00'
            return f + m + s
        else:
            f = str(int(f) + 1)
            if len(f) == 1:
                f = '0' + f
            return f + m + s
    else:
        s = str(int(s) + 1)
        if len(s) == 1:
            s = '0' + s
        return f + m + s


time = input()
a = int(input())
for i in range(a):
    time = inc(time)
print(time)
