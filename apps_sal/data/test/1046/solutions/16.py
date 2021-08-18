secs = int(input())
calls = input().split(' ')
total = 0
calls.sort()
false = 0
for x in range(len(calls) - 2):
    if calls[x] == calls[x + 1] and calls[x] != '0':
        if calls[x + 1] == calls[x + 2] and calls[x + 1] != '0':
            print(-1)
            false = 1
            break
        else:
            total += 1
if false != 1:
    if len(calls) >= 2:
        if calls[len(calls) - 2] == calls[len(calls) - 1] and calls[len(calls) - 1] != '0':
            total += 1
    print(total)
