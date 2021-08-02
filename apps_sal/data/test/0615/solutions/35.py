from statistics import mean

N = int(input())
A = list(map(int, input().split()))

S = [A[0]]
for i in range(1, N):
    S.append(S[i - 1] + A[i])

left_middle = 0
right_middle = 2

ans = float('inf')

for middle in range(1, N - 2):
    left_sum = S[left_middle]
    right_sum = S[middle] - left_sum
    diff = abs(left_sum - right_sum)

    for i in range(left_middle + 1, middle):
        left_sum = S[i]
        right_sum = S[middle] - left_sum
        if diff > abs(left_sum - right_sum):
            left_middle = i
            diff = abs(left_sum - right_sum)
        else:
            break

    left_sum = S[right_middle] - S[middle]
    right_sum = S[-1] - S[right_middle]
    diff = abs(left_sum - right_sum)

    for i in range(right_middle + 1, N):
        left_sum = S[i] - S[middle]
        right_sum = S[-1] - S[i]
        if diff > abs(left_sum - right_sum):
            right_middle = i
            diff = abs(left_sum - right_sum)
        else:
            break

    s1 = S[left_middle]
    s2 = S[middle] - s1
    s3 = S[right_middle] - s1 - s2
    s4 = S[-1] - s1 - s2 - s3

    score = max(s1, s2, s3, s4) - min(s1, s2, s3, s4)
    ans = min(ans, score)

print(ans)
