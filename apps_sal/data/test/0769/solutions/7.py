a, b, c = list(map(int, input('').strip().split()))
occur = dict()
count = 0
for i in range(10 ** 6):
    count += 1
    a *= 10
    occurs = a // b
    occur[a] = occurs
    left = a % b
    if occurs == c:
        print(count)
        break
    else:
        if left * 10 in occur:
            print(-1)
            break
        else:
            a = a % b
