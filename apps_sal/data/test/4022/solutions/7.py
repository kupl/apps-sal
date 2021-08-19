n = int(input())
s = []
s1 = []
for i in range(n):
    (a, b) = list(map(int, input().split()))
    s.append([a, b])
    s1.append([b, a])
s.sort()
s1.sort()
s2 = s.copy()
s3 = s1.copy()
x = s.pop()
s1.remove(x[::-1])
y = s3[0]
s3.remove(y)
s2.remove(y[::-1])
ans = s1[0][0] - s[-1][0]
ans1 = s3[0][0] - s2[-1][0]
if ans > 0 or ans1 > 0:
    print(max(ans, ans1))
else:
    print(0)
