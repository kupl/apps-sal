N = int(input())
A = list(map(int, input().split()))
num = [0] * 10 ** 5
ans = 0
for i in A:
    num[i - 1] += 1
    ans += i
Q = int(input())
for q in range(Q):
    (B, C) = map(int, input().split())
    ans += (C - B) * num[B - 1]
    num[C - 1] += num[B - 1]
    num[B - 1] = 0
    print(ans)
