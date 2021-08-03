N = int(input())
W = list(map(int, input().split()))
total = sum(W)
acc = 0
ans = total
for w in W:
    acc += w
    ans = min(abs(acc - total + acc), ans)
print(ans)
