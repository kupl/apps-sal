n = int(input())
s = input()
timeline = [0] * 1000
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if s[i] == '1':
        for j in range(b):
            timeline[j] += 1
        for j in range(b, 1000, a):
            if (j - b) // a % 2 == 1:
                for k in range(j, min(1000, j + a)):
                    timeline[k] += 1
    else:
        for j in range(b, 1000, a):
            if (j - b) // a % 2 == 0:
                for k in range(j, min(1000, j + a)):
                    timeline[k] += 1
print(max(timeline))
