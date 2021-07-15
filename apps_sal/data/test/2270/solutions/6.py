from collections import defaultdict

spc = {2: 0, 4: 0, 6: 0, 8: 0}
def handle(is_plus, x):
    if is_plus:
        counts[x] += 1
        for v in [2, 4, 6, 8]:
            if counts[x] == v:
                spc[v] += 1
    else:
        counts[x] -= 1
        for v in [2, 4, 6, 8]:
            if counts[x] == v-1:
                spc[v] -= 1

n = int(input())

counts = defaultdict(int)
a = list(map(int, input().split()))
for x in a:
    handle(True, x)

q = int(input())


for _ in range(q):
    c, x = input().split()
    x = int(x)
    
    handle(c=="+", x)
    if spc[8] >= 1:
        print("YES")
    elif spc[6] >= 1 and spc[2] >= 2:
        print("YES")
    elif spc[4] >= 2:
        print("YES")
    elif spc[4] >= 1 and spc[2] >= 3:
        print("YES")
    else:
        print("NO")

