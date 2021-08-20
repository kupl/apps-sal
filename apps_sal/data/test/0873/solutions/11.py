N = int(input())
S1 = input()
S2 = input()


def move(a, b):
    return min(max(a, b) - min(a, b), min(a, b) + 10 - max(a, b))


ans = 0
for i in range(N):
    ans += move(int(S1[i]), int(S2[i]))
print(ans)
