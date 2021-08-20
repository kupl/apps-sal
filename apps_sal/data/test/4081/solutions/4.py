from collections import deque
n = int(input())
A = list(map(int, input().split()))
A = deque(A)
ans = ''
last = 0
while len(A) and (A[0] > last or A[-1] > last):
    if A[0] > last and A[-1] > last:
        if A[0] < A[-1]:
            last = A[0]
            A.popleft()
            ans += 'L'
        else:
            last = A[-1]
            A.pop()
            ans += 'R'
    elif A[0] > last:
        last = A[0]
        A.popleft()
        ans += 'L'
    else:
        last = A[-1]
        A.pop()
        ans += 'R'
print(len(ans))
print(ans)
