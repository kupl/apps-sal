def LI():
    return list(map(int, input().split()))


(X, Y, A, B, C) = LI()
red = LI()
green = LI()
mu = LI()
red.sort(reverse=True)
green.sort(reverse=True)
ans = red[:X] + green[:Y] + mu
ans.sort(reverse=True)
total = 0
for i in range(X + Y):
    total += ans[i]
print(total)
