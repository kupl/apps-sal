N = int(input())
A_list = list(map(int, input().split()))

A_max = A_list[0]
ans = 0

for i in (A_list):
    if i > A_max:
        A_max = i
    elif i < A_max:
        ans += A_max - i

print(ans)
