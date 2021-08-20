N = int(input())
(*A,) = list(map(int, input().split()))
l = [j - i for (i, j) in enumerate(A, start=1)]
l.sort()
b = l[N // 2]
ans = sum((abs(i - b) for i in l))
print(ans)
