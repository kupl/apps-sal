n = int(input())

ai = [int(x) for x in input().split(' ')]

if ai[-1] == 0:
    print('UP')
    return
elif ai[-1] == 15:
    print('DOWN')
    return

if n == 1 and ai[0] not in [0, 15]:
    print(-1)
    return

k = ai[-2:]

if k[0] - k[1] > 0:
    print('DOWN')
else:
    print('UP')

