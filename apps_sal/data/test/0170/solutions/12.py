
n = int(input())
f_deck = list(map(int, input().split(' ')))[1:]
s_deck = list(map(int, input().split(' ')))[1:]

idx = 0
rec = []
while 1:
    rec.append(''.join(list(map(str, f_deck))) + '_' + ''.join(list(map(str, s_deck))))
    if f_deck[0] > s_deck[0]:
        f_deck.append(s_deck.pop(0))
        f_deck.append(f_deck.pop(0))
    else:
        s_deck.append(f_deck.pop(0))
        s_deck.append(s_deck.pop(0))
    idx += 1
    if ''.join(list(map(str, f_deck))) + '_' + ''.join(list(map(str, s_deck))) in rec:
        break
    if len(f_deck) == 0 or len(s_deck) == 0:
        break
if len(f_deck) == 0:
    print("{} {}".format(idx, 2))
elif len(s_deck) == 0:
    print("{} {}".format(idx, 1))
else:
    print(-1)

'''
Input
4
2 1 3
2 4 2
Output
6 2

Input
3
1 2
2 1 3
Output
-1
'''
