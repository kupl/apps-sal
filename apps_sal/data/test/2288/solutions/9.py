for _ in range(int(input())):
    n = int(input())
    aa = list(map(int, input().split()))
    bb = set(map(int, input().split()))
    ans = len(bb) > 1 or aa == sorted(aa)
    print('Yes' if ans else 'No')
