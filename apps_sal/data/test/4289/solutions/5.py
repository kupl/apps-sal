n = int(input())
(t, a) = map(int, input().split())
h = list(map(int, input().split()))
cnt = 0
dict = {}
for i in h:
    cnt += 1
    dict[abs(a - (t - i * 0.006))] = cnt
print(dict[min(dict)])
