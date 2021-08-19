t = int(input())
answers = []
for i in range(t):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    min_koor = 0
    min_dist = a[n - 1] - a[0]
    for j in range(0, n - k):
        if a[j + k] - a[j] <= min_dist:
            min_dist = a[j + k] - a[j]
            min_koor = (a[j] + a[j + k]) / 2
    answers.append(min_koor)
for i in answers:
    print(int(i))
