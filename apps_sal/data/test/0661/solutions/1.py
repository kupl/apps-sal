def main():
    M, K = list(map(int, input().split()))
    if M == 1:
        if K == 0:
            print('0 0 1 1')
        else:
            print('-1')
        return
    if K >= 2 ** M:
        print((-1))
        return
    r = []
    for i in range(2 ** M):
        if i != K:
            r.append(i)
    r.append(K)
    for i in reversed(list(range(2 ** M))):
        if i != K:
            r.append(i)
    r.append(K)
    print((' '.join(str(i) for i in r)))
main()

