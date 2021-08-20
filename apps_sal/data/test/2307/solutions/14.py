def lucky(a):
    count = 0
    for i in a:
        if i % 2 == 0:
            count += 1
    return count > len(a) - count


N = int(input())
a = list(map(int, input().split()))
if lucky(a):
    print('READY FOR BATTLE')
else:
    print('NOT READY')
