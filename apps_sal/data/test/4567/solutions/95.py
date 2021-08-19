N = int(input())
s = []
Sum = 0
for i in range(N):
    s.append(int(input()))
    Sum += s[i]
s.sort()
if Sum % 10 != 0:
    print(Sum)
else:
    for i in range(N):
        if s[i] % 10 != 0:
            print(Sum - s[i])
            break
        if i == N - 1:
            print(0)
