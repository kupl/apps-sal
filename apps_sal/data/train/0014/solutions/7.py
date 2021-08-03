t = int(input())
for tests in range(t):
    a1, b1 = list(map(int, input().split()))
    a2, b2 = list(map(int, input().split()))

    if min(a1, b1) + min(a2, b2) == max(a1, b1) == max(a2, b2):
        print("Yes")
    else:
        print("No")
