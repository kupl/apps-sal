def canJump(numStairs, dirty):
    maxJump = 2
    counter = 0
    dirty.sort()
    if dirty[0] == 1 or dirty[-1] == numStairs:
        return False
    for i in range(1, len(dirty)):
        if dirty[i - 1] + 1 == dirty[i]:
            counter += 1
            if counter >= maxJump:
                break
        else:
            counter = 0
    else:
        return True
    return False


s1 = input()
if int(s1.split(' ')[1]) == 0:
    print('YES')
else:
    s2 = input()
    if canJump(int(s1.split(' ')[0]), [int(s) for s in s2.split(' ')]):
        print('YES')
    else:
        print('NO')
