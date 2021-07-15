n = int(input())
a = []
a = list(map(int, input().split()))
t = [0, 0, 0, 0]
ans = [[], [], [], []]
k = 1
for i in a:
    t[i] += 1
    ans[i].append(k)
    k += 1
size = min(min(t[3], t[1]), t[2]);
print(size)
for i in range(size):
    print(ans[3][i], ans[1][i], ans[2][i])

