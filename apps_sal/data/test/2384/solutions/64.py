N = int(input())
num = list(map(int, input().split()))
dp_odd = [0, num[0]]
dp_even = max(num[0], num[1])
for i in range(2, N):
    if (i + 1) % 2 == 1:
        dp_odd = [max(dp_odd[0] + num[i], dp_even), dp_odd[1] + num[i]]
    else:
        dp_even = max(dp_even + num[i], dp_odd[1])

if N % 2 == 0:
    print(dp_even)
else:
    print(dp_odd[0])
