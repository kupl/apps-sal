N, M, X = map(int, input().split())
A = list(map(int, input().split()))

right = [int(i) for i in A if i > X]
left = [int(i) for i in A if i < X]

r = len(right)
l = len(left)

if r < l:
    print(r)

else:
    print(l)
