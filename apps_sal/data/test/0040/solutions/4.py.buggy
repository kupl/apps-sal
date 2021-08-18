n = int(input())
a = []
a1 = []
for i in range(n):
    f, s = list(map(int, input().split()))
    if f != s:
        print("rated")
        return
    a.append(s)
    a1.append(s)
a.sort()
if a[::-1] == a1:
    print("maybe")
    return
print("unrated")
