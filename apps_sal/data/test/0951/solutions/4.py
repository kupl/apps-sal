(k, n) = (int(input()), input())
n = list(map(int, sorted(list(n))))
s = sum(n) - len(n) * int('0')
if s >= k:
    print('0')
else:
    for i in range(len(n)):
        s += 9 - (n[i] - int('0'))
        if s >= k:
            print(i + 1)
            break
