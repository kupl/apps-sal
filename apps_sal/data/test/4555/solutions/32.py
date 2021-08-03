a, b, k = map(int, input().split())
ans = set()
for i in range(k):
    ans.add(a + i)
    ans.add(b - i)
for i in sorted(list(ans)):
    if a <= i <= b:
        print(i)
