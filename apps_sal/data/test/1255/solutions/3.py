3

def readln(): return tuple(map(int, input().split()))

n, = readln()
cnt = {}
for _ in range(n):
    hm = readln()
    cnt[hm] = cnt.get(hm, 0) + 1
print(max(cnt.values()))

