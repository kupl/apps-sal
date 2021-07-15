N = int(input())
A = list(map(int, input().split()))

ans = sum(A)
num = [0] * (100001)

for a in A:
    num[a] += 1

Q = int(input())

for _ in range(Q):
    B, C = map(int, input().split())
    ans += C * num[B]
    ans -= B * num[B]
    num[C] += num[B]
    num[B] = 0
    print(ans)
