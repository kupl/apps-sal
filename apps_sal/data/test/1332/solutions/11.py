arr = list(map(int ,input().split()))
l = len(arr)
s = sum(arr)
if s % l != 0 or s == 0:
    print(-1)
else:
    print(s // l)
