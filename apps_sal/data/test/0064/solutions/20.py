from collections import Counter

balls_nr, friends_nr = (int(x) for x in input().split())
ball_idx___color = input()
if max(Counter(ball_idx___color).values()) > friends_nr:
    print('NO')
else:
    print('YES')


