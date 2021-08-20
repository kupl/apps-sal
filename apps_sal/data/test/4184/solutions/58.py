N = input()
W = list(map(int, input().split()))
total = sum(W)
acc = 0
ans = total
for i in W:
    acc += i
    ans = min(abs(acc - total + acc), ans)
print(ans)
