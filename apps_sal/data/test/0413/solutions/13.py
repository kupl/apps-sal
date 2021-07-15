m, n = [int(i) for i in input().split()]

def d(begin, end):
   #print(begin, end)
    if begin == end:
       return 0

    if begin == end + 1:
        return 1

    if end % 2 == 0 and end // 2 == begin:
        return 1

    if begin > end:
        return begin - end

    if end % 2 == 0:
        return d(begin, end // 2) + 1

    return d(begin, end + 1) + 1

print(d(m, n))






















