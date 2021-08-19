n = int(input())
A = list(map(int, input().split()))
sum_left_odd = [0] * (n + 1)
sum_left_even = [0] * (n + 1)
sum_right_odd = [0] * (n + 1)
sum_right_even = [0] * (n + 1)
for i in range(n):
    if i % 2 == 0:
        sum_left_even[i] = sum_left_even[i - 1] + A[i]
        sum_left_odd[i] = sum_left_odd[i - 1]
    else:
        sum_left_even[i] = sum_left_even[i - 1]
        sum_left_odd[i] = sum_left_odd[i - 1] + A[i]
B = A[::-1]
for i in range(n):
    if i % 2 == 0:
        sum_right_even[i] = sum_right_even[i - 1] + B[i]
        sum_right_odd[i] = sum_right_odd[i - 1]
    else:
        sum_right_even[i] = sum_right_even[i - 1]
        sum_right_odd[i] = sum_right_odd[i - 1] + B[i]
answer = 0
for i in range(n):
    if n % 2:
        answer += int(sum_left_odd[i] + sum_right_even[n - i - 1] == sum_left_even[i] + sum_right_odd[n - i - 1])
    else:
        answer += int(sum_left_odd[i] + sum_right_odd[n - i - 1] == sum_left_even[i] + sum_right_even[n - i - 1])
print(answer)
