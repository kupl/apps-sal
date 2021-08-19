N = int(input())
A = list(map(int, input().split()))
ans = []
ptr = 0
while ptr < N:
    s = 0
    nxt = ptr
    while nxt < N and s + (A[nxt] < 0) <= 2:
        s += A[nxt] < 0
        nxt += 1
    ans.append(nxt - ptr)
    ptr = nxt
print(len(ans))
print(*ans)
