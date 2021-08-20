t = int(input())
Ans = []
for _ in range(t):
    (n, k) = map(int, input().split())
    A = list(map(int, input().split()))
    mini = 100000000000
    for i in range(n - k):
        y1 = (-A[i] + A[i + k] - 1) / 2
        y2 = (-A[i] + A[i + k]) / 2
        if float.is_integer(y1):
            if mini > y1 + 1:
                ans = A[i] + y1
                mini = y1 + 1
        elif float.is_integer(y2):
            if mini > y2:
                ans = A[i] + y2
                mini = y2
    Ans.append(int(ans))
print(*Ans, sep='\n')
