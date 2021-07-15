from collections import deque
n = int(input())
A = list(map(int, input().split()))
A = deque(A)
ans = ''
last = 0
while len(A) and (A[0] > last or A[-1] > last):
    if len(A) == 1:
        ans += 'R'
        break
    if A[0] > last and A[-1] > last:
        if A[0] < A[-1]:
            last = A[0]
            A.popleft()
            ans += 'L'
        elif A[-1] < A[0]:
            last = A[-1]
            A.pop()
            ans += 'R'
        else:
            lal = last
            cnt1 = -1
            for i in A:
                cnt1 += 1
                if i > lal:
                    lal = i
                else:
                    break
            lol = last
            cnt2 = -1
            for i in range(len(A) - 1, -1, -1):
                cnt2 += 1
                if A[i] > lol:
                    lol = A[i]
                else:
                    break
            if cnt1 > cnt2:
                ans += 'L' * cnt1
            else:
                ans += 'R' * cnt2
            break
    else:
        if A[0] > last:
            last = A[0]
            A.popleft()
            ans += 'L'
        else:
            last = A[-1]
            A.pop()
            ans += 'R'
print(len(ans))
print(ans)

