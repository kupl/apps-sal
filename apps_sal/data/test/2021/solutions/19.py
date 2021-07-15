n = int(input())
a = list(map(int, input().split()))
s = sum(a)
a.sort(reverse=True)
m = int(input())
q = list(map(int, input().split()))
for i in q:
    print(s - a[i - 1])
