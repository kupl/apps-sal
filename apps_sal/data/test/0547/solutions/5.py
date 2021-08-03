n, k = list(map(int, input().split()))
s = [input() for i in range(n)]
pas = input()
a = sorted([len(i) for i in s])
def f(x): return x + ((x - 1) // k) * 5


for i in range(n):
    if a[i] == len(pas):
        L = i + 1
        break
ans1 = f(L)
R = n
for i in range(n):
    if a[i] > len(pas):
        R = i
        break
ans2 = f(R)
print(ans1, ans2)
