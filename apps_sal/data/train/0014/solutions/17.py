q = int(input())
for i in range(q):
    (a1, b1) = map(int, input().split())
    (a2, b2) = map(int, input().split())
    if max(a1, b1) == max(a2, b2) == min(a1, b1) + min(a2, b2):
        print('Yes')
    else:
        print('No')
