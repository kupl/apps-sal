n, ss = map(int, input().split())
buy, send = dict(), dict()
for i in range(n):
    s = list(map(str, input().split()))
    c_v = list(map(int, s[1:]))
    if s[0] == 'B':
        if c_v[0] in buy:
            buy[c_v[0]] += c_v[1]
        else:
            buy[c_v[0]] = c_v[1]
    else:
        if c_v[0] in send:
            send[c_v[0]] += c_v[1]
        else:
            send[c_v[0]] = c_v[1]
length_s, length_b = len(send), len(buy)
buy_ = sorted(buy)[0 if length_b < ss else length_b - ss:]
send_ = sorted(send)[:min(length_s, ss)]
for i in range(len(send_) - 1, -1, -1):
    print('S', send_[i], send[send_[i]])
for i in range(len(buy_) - 1, -1, -1):
    print('B', buy_[i], buy[buy_[i]])
