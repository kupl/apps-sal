has = [input() for _ in range(int(input()))]
lens = int(input())
B = input()
cnt = 0
alls = set()
for i in range(lens):
    for j in range(i, lens):
        curr = B[i:j + 1]
        if curr in alls: continue
        cnt += curr in has
        alls.add(curr)
print(cnt)
