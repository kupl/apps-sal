def count1(n):
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
    return count


def find(n, k):
    ones = count1(n)
    l = list()
    if ones > k:
        print('No')
    else:
        tmp = n
        pow2 = 1
        index = 0
        while tmp > 0:
            if tmp % 2 == 1:
                l.append(index)
            tmp //= 2
            pow2 *= 2
            index += 1
        length = len(l)
        while length < k:
            m = max(l)
            c = l.count(m)
            rem = [i for i in l if i < m]
            if k - length >= c:
                rem += [m - 1] * (2 * c)
                l = rem
                length = len(l)
            else:
                mini = min(l)
                to_fill = k - length
                l.remove(mini)
                for i in range(to_fill):
                    mini -= 1
                    l.append(mini)
                l.append(mini)
                break
        print('Yes')
        l.sort(reverse=True)
        print(' '.join([str(i) for i in l]))


nn, kk = list(map(int, input().strip().split()))
find(nn, kk)
