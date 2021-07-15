#def test(l):
#    n = len(l)
#    c = 0
#    while max(l) >= n:
#        l.sort()
#        l[-1] -= n
#        for i in range(n-1):
#            l[i] += 1
#        c += 1
#    return c

def main():
    K = int(input())
    if K <= 49:
        print((50))
        l = [0] * (50 - K) + [50] * K
        print((' '.join(str(i) for i in l)))
        return l
    l = [(K // 50) + 50] * 50
    a = 50 - K % 50
    for i in range(a):
        l[0] -= 50
        for j in range(1, 50):
            l[j] += 1
        l.sort(reverse=True)
    print((50))
    print((' '.join(str(i) for i in l)))
    return l
l = main()
#print('kotae', test(l))

