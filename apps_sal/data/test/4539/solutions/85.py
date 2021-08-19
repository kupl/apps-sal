def d(num):
    l = [int(x) for x in str(num)]
    return sum(l)


n = int(input())
print('Yes' if n % d(n) == 0 else 'No')
