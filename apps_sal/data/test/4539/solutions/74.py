def digitsum(n):
    return sum(list(map(int, list(str(n)))))


N = int(input())
if N % digitsum(N) == 0:
    print('Yes')
else:
    print('No')
