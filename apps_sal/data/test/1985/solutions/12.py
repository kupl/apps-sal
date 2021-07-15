from sys import stdin, stdout

k, n = map(int, stdin.readline().split())
marks = list(map(int, stdin.readline().split()))
values = list(map(int, stdin.readline().split()))

cnt = [marks[0]]
for i in range(1, k):
    cnt.append(cnt[-1] + marks[i])

cnt.sort()
values.sort()
ans = set()

for i in range(k - n + 1):
    x = values[0] - cnt[i]
    
    pos = 1
    ind = i + 1
    label = 1
    
    while pos < n and ind < k:
        if cnt[ind] + x < values[pos]:
            ind += 1
        elif cnt[ind] + x == values[pos]:
            ind += 1
            pos += 1
        else:
            label = 0
            break
    
    if label and pos == n:
        ans.add(x)

stdout.write(str(len(ans)))
