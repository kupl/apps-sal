N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 1

for i in A:
    ans *= i
    if ans > 10 ** 18:
        print((-1))
        break
else:
    print(ans)
