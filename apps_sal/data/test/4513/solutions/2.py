Q = int(input())
for q in range(Q):
    s = [input().replace('2', '1') for i in range(9)]
    for i in s: print(i)

