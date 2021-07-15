topboard = list(input())
botboard = list(input())

bish = 0
left = 0
while left + 1 < len(topboard):
    if topboard[left] == '0' and botboard[left] == '0':
        if topboard[left+1] == '0':
            bish += 1
            topboard[left] = 'X'
            topboard[left+1] = 'X'
            botboard[left] = 'X'
        elif botboard[left+1] == '0':
            bish += 1
            topboard[left] = 'X'
            botboard[left] = 'X'
            botboard[left+1] = 'X'
    elif topboard[left+1] == '0' and botboard[left+1] == '0':
        if topboard[left] == '0':
            bish += 1
            topboard[left] = 'X'
            topboard[left+1] = 'X'
            botboard[left+1] = 'X'
        elif botboard[left] == '0':
            bish += 1
            topboard[left+1] = 'X'
            botboard[left] = 'X'
            botboard[left+1] = 'X'

    left += 1

print(bish)

