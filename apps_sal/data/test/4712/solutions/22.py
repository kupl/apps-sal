(H, W) = list(map(int, input().split()))
ans = []
for _ in range(H):
    a = input()
    ans.append('#' + a + '#')
print('#' * (W + 2))
for i in range(H):
    print(ans[i])
print('#' * (W + 2))
