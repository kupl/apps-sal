t = int(input())
for case_num in range(t):
    a, b = list(map(int, input().split(' ')))
    print((b - a % b) % b)
