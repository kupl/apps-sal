N = int(input())
A = list(map(int, input().split()))
answer = 1

if 0 in A:
    print((0))
    return

for i in range(N):
    answer *= A[i]
    if answer > 10**18:
        print((-1))
        return

print(answer)
