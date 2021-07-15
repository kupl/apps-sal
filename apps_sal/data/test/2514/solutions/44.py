N = int(input())
A = input().split()
num_list = [0] * 10**5
ans = 0

for i in range(N):
    num_list[int(A[i])-1] += 1

for i in range(10**5):
    ans += (i+1) * num_list[i]

Q = int(input())

for i in range(Q):
    B, C = map(int, input().split())

    ans = ans + C * num_list[B-1] - B * num_list[B-1]
    num_list[C-1] += num_list[B-1]
    num_list[B-1] = 0

    print(ans)
