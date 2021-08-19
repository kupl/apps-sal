(n, k) = map(int, input().split())
(r, s, p) = map(int, input().split())
t = input()
point = {'r': (p, 'p'), 's': (r, 'r'), 'p': (s, 's')}
ans = 0
hand = ''
for i in range(n):
    if i < k:
        ans += point[t[i]][0]
        hand += point[t[i]][1]
    elif t[i - k] != t[i]:
        ans += point[t[i]][0]
        hand += point[t[i]][1]
    elif hand[i - k] != point[t[i]][1]:
        ans += point[t[i]][0]
        hand += point[t[i]][1]
    elif i + k < n:
        hand += 'rsp'.replace(point[t[i + k]][1], '').replace(hand[i - k], '')[0]
    else:
        hand += 'rsp'.replace(hand[i - k], '')[0]
print(ans)
