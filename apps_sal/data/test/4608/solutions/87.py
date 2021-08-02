N = int(input())
A = [int(input()) - 1 for _ in range(N)]
cnt = 1
next_button = 0
while cnt <= len(A):
    next_button = A[next_button]
    if next_button == 1:
        print(cnt)
        return
    cnt += 1
print((-1))
