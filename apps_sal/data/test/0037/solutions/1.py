a, b, c = list(map(int, input().split()))

T = [not((c - a * k) % b) for k in range(c // a + 1)]

if sum(T):
    print("Yes")
else:
    print("No")
